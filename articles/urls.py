from django.urls import path
from .viewsets import *


# from rest_framework.routers import SimpleRouter



# routes = SimpleRouter()

# # AUTHENTICATION
# routes.register('auth/login', LoginViewSet, basename='auth-login')
# routes.register('auth/register', RegistrationViewSet, basename='auth-register')
# routes.register('auth/refresh', RefreshViewSet, basename='auth-refresh')


urlpatterns = [
    path('api/user/', UserDetailView.as_view()),

    path('api/article/', ArticleView.as_view({'post': 'create'})),
    path('api/articles/', ArticleView.as_view({'get': 'list'})),
    path('api/article/<str:pk>/', ArticleView.as_view({'get': 'retrieve'})),

    path('api/comment/', CommentView.as_view({'post': 'create'})),
    path('api/comments/', CommentView.as_view({'get': 'list'})),
    path('api/comments/<str:pk>/', CommentView.as_view({'get': 'list'})),
    path('api/comment/<str:pk>/', CommentView.as_view({'get': 'retrieve'})),


    # *routes.urls
]