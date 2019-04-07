# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gomaku.serializers import *
from rest_framework import mixins, generics, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt,csrf_protect


class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    查询或更新用户
    可按照ID和名字进行查询 ID完全匹配 名字部分匹配
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=userId', 'name')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    查看用户详情
    更改用户以及删除用户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GameList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GameDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FriendList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('me', 'friend')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FriendDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@csrf_exempt
@api_view(['POST'])
def login(request):
    userId = request.data.get('userId')
    pwd = request.data.get('pwd')
    msg = None
    succ = False
    if userId and pwd:
        user = User.objects.get(userId=userId)
        if user and user.pwd == pwd:
            user.online = True
            user.save()
            succ = True
        else:
            msg = 'User is not existed or password is incorrect'
            succ = False
    return Response({
        'msg': msg,
        'succ': succ
    }, status=status.HTTP_202_ACCEPTED)


@csrf_exempt
@api_view(['GET'])
def logout(request):
    userId = request.GET.get('userId')
    if userId:
        user = User.objects.get(userId=userId)
        if user:
            user.online = False
            user.save()
    return Response(status=status.HTTP_202_ACCEPTED)


