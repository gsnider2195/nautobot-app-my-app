"""Django urlpatterns declaration for my_app app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from my_app import views


router = NautobotUIViewSetRouter()

router.register("testmodel", views.TestModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("my_app/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
