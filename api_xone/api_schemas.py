from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import LinkSerializer, CollectionSerializer

link_list_schema = extend_schema(
    operation_id="list_links",
    summary="List all links",
    description="Endpoint to list all links for the authenticated user.",
    responses={200: LinkSerializer(many=True)},
    parameters=[
        OpenApiParameter(
            name='Authorization',
            description='Bearer token',
            required=True,
            type=str,
            location=OpenApiParameter.HEADER
        ),
    ],
)

link_create_schema = extend_schema(
    operation_id="create_link",
    summary="Create a new link",
    description="Endpoint to create a new link for the authenticated user.",
    request=LinkSerializer,
    responses={201: LinkSerializer},
    parameters=[
        OpenApiParameter(
            name='Authorization',
            description='Bearer token',
            required=True,
            type=str,
            location=OpenApiParameter.HEADER
        ),
    ],
)

collection_list_schema = extend_schema(
    operation_id="list_collections",
    summary="List all collections",
    description="Endpoint to list all collections for the authenticated user.",
    responses={200: CollectionSerializer(many=True)},
    parameters=[
        OpenApiParameter(
            name='Authorization',
            description='Bearer token',
            required=True,
            type=str,
            location=OpenApiParameter.HEADER
        ),
    ],
)

collection_create_schema = extend_schema(
    operation_id="create_collection",
    summary="Create a new collection",
    description="Endpoint to create a new collection for the authenticated user.",
    request=CollectionSerializer,
    responses={201: CollectionSerializer},
    parameters=[
        OpenApiParameter(
            name='Authorization',
            description='Bearer token',
            required=True,
            type=str,
            location=OpenApiParameter.HEADER
        ),
    ],
)
collection_retrieve_schema = extend_schema(
    operation_id="retrieve_collection",
    summary="Retrieve a collection",
    description="Endpoint to retrieve a collection by ID for the authenticated user.",
    responses={200: CollectionSerializer}
)

collection_update_schema = extend_schema(
    operation_id="update_collection",
    summary="Update a collection",
    description="Endpoint to update a collection by ID for the authenticated user.",
    responses={200: CollectionSerializer}
)

collection_partial_update_schema = extend_schema(
    operation_id="partial_update_collection",
    summary="Partially update a collection",
    description="Endpoint to partially update a collection by ID for the authenticated user.",
    responses={200: CollectionSerializer}
)

collection_destroy_schema = extend_schema(
    operation_id="destroy_collection",
    summary="Delete a collection",
    description="Endpoint to delete a collection by ID for the authenticated user.",
    responses={204: None}
)
link_retrieve_schema = extend_schema(
    operation_id="retrieve_link",
    summary="Retrieve a link",
    description="Endpoint to retrieve a link by ID for the authenticated user.",
    responses={200: LinkSerializer}
)

link_update_schema = extend_schema(
    operation_id="update_link",
    summary="Update a link",
    description="Endpoint to update a link by ID for the authenticated user.",
    responses={200: LinkSerializer}
)

link_partial_update_schema = extend_schema(
    operation_id="partial_update_link",
    summary="Partially update a link",
    description="Endpoint to partially update a link by ID for the authenticated user.",
    responses={200: LinkSerializer}
)

link_destroy_schema = extend_schema(
    operation_id="destroy_link",
    summary="Delete a link",
    description="Endpoint to delete a link by ID for the authenticated user.",
    responses={204: None}
)
