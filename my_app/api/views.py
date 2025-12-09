"""API views for my_app."""

from nautobot.apps.api import NautobotModelViewSet

from my_app import filters, models
from my_app.api import serializers


class TestModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """TestModel viewset."""

    queryset = models.TestModel.objects.all()
    serializer_class = serializers.TestModelSerializer
    filterset_class = filters.TestModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
