from rest_framework import viewsets, permissions

from .models import Link, Collection
from .api_schemas import (
    link_list_schema, link_create_schema, link_retrieve_schema, link_update_schema,
    link_partial_update_schema, link_destroy_schema,
    collection_list_schema, collection_create_schema,
    collection_retrieve_schema, collection_update_schema,
    collection_partial_update_schema, collection_destroy_schema
)
from .serializers import LinkSerializer, CollectionSerializer
from .utils import fetch_link_metadata


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    @link_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @link_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @link_retrieve_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @link_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @link_partial_update_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @link_destroy_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        link_data = fetch_link_metadata(self.request.data['url'])
        serializer.save(user=self.request.user, **link_data)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @collection_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @collection_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @collection_retrieve_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @collection_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @collection_partial_update_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @collection_destroy_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)