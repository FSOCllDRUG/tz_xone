from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, ChangePasswordSerializer, MyTokenObtainPairSerializer, PasswordResetSerializer, \
    PasswordResetConfirmSerializer

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"status": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PasswordResetView(APIView):
    @extend_schema(
        request=PasswordResetSerializer,
        responses={
            200: OpenApiExample(
                'Password reset link sent to your email',
                value={'message': 'Password reset link sent to your email'},
                media_type="application/json"
            ),
            404: OpenApiExample(
                'User with this email not found',
                value={'message': 'User with this email not found'},
                media_type="application/json"
            ),
            400: OpenApiExample(
                'Email is required',
                value={'message': 'Email is required'},
                media_type="application/json"
            ),
        }
    )
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email).first()
        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = f"http://localhost:8000/api/auth/password-reset-confirm/{uidb64}/{token}"
            send_mail(
                'Password Reset',
                f'Link: {link}\n'
                'Please send new password via link using POST method:\n'
                'JSON\n'
                '{\n'
                '"new_password": "ur_new_password"'
                '\n}',
                'XOne Team',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset link sent to your email'}, status=status.HTTP_200_OK)
        return Response({'message': 'User with this email not found'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetConfirmView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='uidb64',
                description='Base64-encoded user ID',
                required=True,
                type=str,
                location=OpenApiParameter.PATH
            ),
            OpenApiParameter(
                name='token',
                description='Password reset token',
                required=True,
                type=str,
                location=OpenApiParameter.PATH
            ),
        ],
        request=PasswordResetConfirmSerializer,
        responses={
            200: OpenApiExample(
                'Password reset successfully',
                value={'message': 'Password reset successfully'},
                media_type="application/json"
            ),
            400: OpenApiExample(
                'Invalid token or user',
                value={'message': 'Invalid token or user'},
                media_type="application/json"
            ),
        }
    )
    def post(self, request, uidb64, token):
        try:
            user_id = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and PasswordResetTokenGenerator().check_token(user, token):
            new_password = request.data.get('new_password')
            if not new_password:
                return Response({'message': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)
