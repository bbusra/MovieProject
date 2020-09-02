from django.urls import path
from . import views
from django.views.generic import TemplateView

# 127.0.0.1:8000/movies
# 127.0.0.1:8000/movies/2
# 127.0.0.1:8000/movies/search

urlpatterns = [
    path('', views.index , name= 'movies'),
    path('<int:movie_id>', views.detail, name= 'detail'),
    path('search', views.search, name= 'search'),
     path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
