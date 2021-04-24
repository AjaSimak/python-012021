from django.urls import path
from. import views

urlpatterns = [
  path("", views.MujPrvniUkol.as_view(), name="index"),
  path("", views.KontaktyView.as_view(), name="index"),
  path("organizace/", views.OrganizaceView.as_view(), name="organizace")
]