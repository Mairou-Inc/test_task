from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Article API')

urlpatterns = [
    path('api/doc/', get_swagger_view(title='Rest API')),
    path('admin/', admin.site.urls),
    path('', include("articles.urls")),

]
