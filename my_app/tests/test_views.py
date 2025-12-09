"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from my_app import models
from my_app.tests import fixtures


class TestModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the TestModel views."""

    model = models.TestModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_testmodel()
