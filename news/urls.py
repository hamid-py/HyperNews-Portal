from django.urls import path
from .views import ViewsNewsLink, StarterView, AdressView, CreateVew

urlpatterns = [
    path('', StarterView.as_view()),
    path('news/', AdressView.as_view()),
    path('news/create/', CreateVew.as_view() ),
    path('news/<int:link_number>/', ViewsNewsLink.as_view())

]
