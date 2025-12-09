"""Create fixtures for tests."""

from my_app.models import TestModel


def create_testmodel():
    """Fixture to create necessary number of TestModel for tests."""
    TestModel.objects.create(name="Test One")
    TestModel.objects.create(name="Test Two")
    TestModel.objects.create(name="Test Three")
