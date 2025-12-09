"""Filtering for my_app."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from my_app import models


class TestModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for TestModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.TestModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
