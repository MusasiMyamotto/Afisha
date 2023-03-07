from django.contrib import admin
from django.urls import path
from movie_app.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', MovieListAPIView.as_view()),
    path('api/v1/movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', ReviewMoviesView.as_view()),
    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),
]
