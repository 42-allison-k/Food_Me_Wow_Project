from django.urls import path
from food_review.views import HomePageView, SearchView, RestaurantProfile, AddRestaurantView, Comments

urlpatterns = [
   
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name='search'),
    path("restaurant/<int:restaurant_id>",
         RestaurantProfile.as_view(), name='restaurant'),
    path('add/', AddRestaurantView.as_view(), name='add'),
    path("restaurant/<int:restaurant_id>/comment/<int:comment_id>",
         Comments.as_view(), name='comment'),
]