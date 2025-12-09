"""Forms for my_app."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from my_app import models


class TestModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """TestModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.TestModel
        fields = [
            "name",
            "description",
        ]


class TestModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """TestModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.TestModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class TestModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.TestModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
