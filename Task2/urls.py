from django.urls import path,include
from rest_frame.routers import DefaultRouter
from .views import TaskviewSet

router=DefaultRouter()
router.register(r'tasks',TaskviewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]
