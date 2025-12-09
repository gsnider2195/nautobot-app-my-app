"""Unit tests for my_app."""

from nautobot.apps.testing import APIViewTestCases

from my_app import models
from my_app.tests import fixtures


class TestModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for TestModel."""

    model = models.TestModel
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_testmodel()
