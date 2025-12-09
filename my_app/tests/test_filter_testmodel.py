"""Test TestModel Filter."""

from django.test import TestCase

from my_app import filters, models
from my_app.tests import fixtures


class TestModelFilterTestCase(TestCase):
    """TestModel Filter Test Case."""

    queryset = models.TestModel.objects.all()
    filterset = filters.TestModelFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for TestModel Model."""
        fixtures.create_testmodel()

    def test_q_search_name(self):
        """Test using Q search with name of TestModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for TestModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
