"""Views for my_app."""

from nautobot.apps.views import NautobotUIViewSet

from my_app import filters, forms, models, tables
from my_app.api import serializers


class TestModelUIViewSet(NautobotUIViewSet):
    """ViewSet for TestModel views."""

    bulk_update_form_class = forms.TestModelBulkEditForm
    filterset_class = filters.TestModelFilterSet
    filterset_form_class = forms.TestModelFilterForm
    form_class = forms.TestModelForm
    lookup_field = "pk"
    queryset = models.TestModel.objects.all()
    serializer_class = serializers.TestModelSerializer
    table_class = tables.TestModelTable
