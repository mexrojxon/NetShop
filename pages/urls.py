from django.urls import path
from .views import HomePageView, AboutUsView, ContactView

app_name = "pages"

urlpatterns = [
    path('', HomePageView.as_view(), name='home', ),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
