from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'', AlumnoViewSet)


urlpatterns = [
    path('form/', formView, name="form"),
    path('', include(router.urls))
]

