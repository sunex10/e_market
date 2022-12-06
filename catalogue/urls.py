from django.urls import path
from .views import Info, Products, About, Contacts, LatestPhone,UkusedPhones, ProductDetails

urlpatterns = [
    path("", Products, name="product"),
    path("product/", Products, name="product"),
    path("infomation/", Info.as_view(), name="information"),
    path("about/",  About.as_view(), name="about"),
    path("contacts/",  Contacts.as_view(), name="contacts"),
    path("latest_phone/",  LatestPhone, name="latest_phone"),
    path("Ukusedphones/", UkusedPhones, name="Uk_used_phones"),
    path("details/<str:id>/", ProductDetails, name="details")
] 