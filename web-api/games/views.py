from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Game, Player, GamePlayer
from .serializers import ( GameSerializer, PlayerSerializer, PlayerCreateSerializer, PlayerUpdateSerializer, 
                           GamePlayerReadOnlySerializer, PlayerSearchSerializer, PlayerFriendSerializer,
                           PlayerFriendUpdateSerializer, )

from .permissions import IsOwnerOrReadOnly, IsSameUser, IsFriend

class GamePlayerList(generics.ListAPIView):
    ## HACER TESTS
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = GamePlayerReadOnlySerializer

    def get_queryset(self):
        user = self.request.user
        return user.gameplayer_set.all()


class GameList(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if not obj.players.filter(id = obj.owner.id).exists():
            game_player = GamePlayer.objects.create(player = obj.owner, game = obj, player_invitation_status = True)
            game_player.save()

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user

class PlayerList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerCreate(generics.CreateAPIView):
    serializer_class = PlayerCreateSerializer

class PlayerUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsSameUser,)
    queryset = Player.objects.all()
    serializer_class = PlayerUpdateSerializer

class PlayerListSearch(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PlayerSearchSerializer

    def get_queryset(self):
        user = self.request.user
        username = self.kwargs['username'].strip()
        if len(username) == 0:
          return []

        return Player.objects.exclude(id = user.id).filter(username__icontains=username)

class PlayerFriendsList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PlayerSearchSerializer

    def get_queryset(self):
        user = self.request.user
        return user.get_all_friends()

class PlayerFriendCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PlayerFriendSerializer

    def pre_save(self, obj):
        obj.player = self.request.user

class PlayerFriendUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsFriend)
    serializer_class = PlayerFriendUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return user.friend.filter(status = None)

from rest_framework.decorators import api_view
from social.apps.django_app.utils import strategy

@strategy()
@api_view(['POST'])
def social_register(request, backend):
    auth_token = request.DATA.get('access_token', None)
    if auth_token:
        try:
            user = request.strategy.backend.do_auth(access_token=auth_token)
        except Exception, err:
            return Response(str(err), status=400)

        if user:
          return Response({ 'token': user.auth_token.key, 'username': user.username },  status=status.HTTP_200_OK )
        else:
            return Response("Bad Credentials", status=403)
    else:
        return Response("Bad request", status=400)

