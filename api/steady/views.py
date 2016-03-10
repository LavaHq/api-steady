from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Foo
from api.steady.serializers import UserSerializer, GroupSerializer, FooSerializer


@api_view(['GET', 'POST'])
def foo_list(request):
    if request.method == 'GET':
        tasks = Foo.objects.all()
        serializer = FooSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FooSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Failed')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
