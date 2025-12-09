"""Test TestModel."""

from django.test import TestCase

from my_app import models


class TestTestModel(TestCase):
    """Test TestModel."""

    def test_create_testmodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        testmodel = models.TestModel.objects.create(name="Development")
        self.assertEqual(testmodel.name, "Development")
        self.assertEqual(testmodel.description, "")
        self.assertEqual(str(testmodel), "Development")

    def test_create_testmodel_all_fields_success(self):
        """Create TestModel with all fields."""
        testmodel = models.TestModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(testmodel.name, "Development")
        self.assertEqual(testmodel.description, "Development Test")
