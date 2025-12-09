"""Django API urlpatterns declaration for my_app app."""

from nautobot.apps.api import OrderedDefaultRouter

from my_app.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("testmodel", views.TestModelViewSet)

urlpatterns = router.urls
