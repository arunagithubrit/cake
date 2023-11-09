from django.urls import path
from cakeapp_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('cakes',views.CakesView,basename='cakes')
urlpatterns=[
    path('register/',views.UserCreationView.as_view())
]+router.urls