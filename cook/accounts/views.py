
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from djoser.views import UserViewSet as DjoserUserViewSet

from drf_yasg.utils import swagger_auto_schema

from accounts.models import User
from .serializers import UserAPISerializer, UserCreateAPISerializer


class UserCreateView(DjoserUserViewSet):
    """
    Custom view for user registration using Djoser.
    """
    serializer_class = UserCreateAPISerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserMeAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAPISerializer

    @swagger_auto_schema(tags=['users'])
    def retrieve(self, request):
        if not request.user.is_authenticated:
            return Response(data='Not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_serializer(request.user).data
        return Response(data=user)
