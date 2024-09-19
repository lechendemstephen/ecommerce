from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path("<slug:product_slug>/", views.product_detail, name="single_product")

]
