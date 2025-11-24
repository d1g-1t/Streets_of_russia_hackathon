import logging
import sys

from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializers import MyAuthSerializer

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s - строка %(lineno)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.disabled = False
logger.debug('Логирование из myauth.views запущено')


class MyAuth(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = MyAuthSerializer(
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'auth_token': token.key},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUnAuth(views.APIView):
    def post(self, request):
        token = get_object_or_404(Token, key=request.auth)
        token.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
