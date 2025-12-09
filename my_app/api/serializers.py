"""API serializers for my_app."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from my_app import models


class TestModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """TestModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.TestModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
