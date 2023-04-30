from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from djoser.views import UserViewSet
from .views import UserCreateView

# from accounts.views import UserViewSet, UserMeAPIView
from djoser import views



# # router = SimpleRouter()
# # router.register('users', UserViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view({'post': 'create'}), name='register'),
#     path('auth/', include('djoser.urls')),
#     re_path(r'^auth/', include('djoser.urls.authtoken'))
# #     path('users/me/', UserMeAPIView.as_view(), name='me'),
]
# # urlpatterns += router.urls