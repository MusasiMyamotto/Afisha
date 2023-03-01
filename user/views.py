from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user.serializers import UserValidateSerializer, UserCreateSerializer


@api_view(['POST'])
def confirm_user_api_view(request):
    code = request.data.get('code')
    if not code:
        return Response({'error': 'Code is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, confirmation_code=code)
    if user.is_active:
        return Response({'error': 'User is already active'}, status=status.HTTP_400_BAD_REQUEST)

    user.is_active = True
    user.confirmation_code = ''
    user.save()
    return Response({'success': 'User has been confirmed'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error message': 'User Not Found!'})


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)