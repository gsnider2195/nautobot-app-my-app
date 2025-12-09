"""Test testmodel forms."""

from django.test import TestCase

from my_app import forms


class TestModelTest(TestCase):
    """Test TestModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.TestModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.TestModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_testmodel_is_required(self):
        form = forms.TestModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
