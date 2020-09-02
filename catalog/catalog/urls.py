"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from movies import views
from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='Movie API')

router = routers.DefaultRouter()
router.register(r'filmler', views.MovieViewSet)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# drf_yasg code starts here
schema_view = get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version='v1',
        description="Welcome to Movie API ",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here
from rest_framework.schemas import get_schema_view
urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    #path('docs/', schema_view), #HERE
    path('',include('pages.urls')), # burada 'pages/' yazarsak sabit olacak (pages->urls de boşluk vardı)
    path('movies/',include('movies.urls')),
    path('user/',include('user.urls')),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="Movies-List",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    url(r'admin/', admin.site.urls),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(router.urls))
]