from django.contrib import admin
from django.urls import path
from movie_app.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_list_api_view),
    path('api/v1/directors/<int:id>/', director_detail_api_view),
    path('api/v1/movies/', movie_list_api_view),
    path('api/v1/movies/<int:id>/', movie_detail_api_view),
    path('api/v1/reviews/', review_list_api_view),
    path('api/v1/reviews/<int:id>/', review_detail_api_view),
    path('api/v1/movies/reviews/', review_movies_view),
    path('api/v1/users/registration/', registration_api_view),
    path('api/v1/users/confirm/', confirm_user_api_view),
    path('api/v1/users/authorization/', authorization_api_view),
]
