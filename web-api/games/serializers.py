from rest_framework import serializers
from .models import Game, Player, GamePlayer

class GamePlayerSerializer(serializers.ModelSerializer):
    id = serializers.Field(source = 'player.id')
    username = serializers.Field(source = 'player.username')

    class Meta:
        model = GamePlayer
        fields = ('player', 'username',)

class GameSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source = 'owner.username')
    tournament_name = serializers.Field(source = 'tournament.name')

    gameplayers =  GamePlayerSerializer(source="gameplayer_set", many = True)

    class Meta:
        model = Game
        fields  = ('id', 'owner', 'name', 'tournament', 'tournament_name', 'gameplayers')

class GamePlayerReadOnlySerializer(serializers.ModelSerializer):
    username = serializers.Field(source = 'player.username')

    class Meta:
        model = GamePlayer
        fields = ('player', 'username', 'game', 'player_invitation_status',)

GamePlayerReadOnlySerializer.base_fields['game'] = GameSerializer()

class PlayerSerializer(serializers.ModelSerializer):
#    games = serializers.PrimaryKeyRelatedField(many = True)
#    owner_games = serializers.PrimaryKeyRelatedField(many = True)
#    GamePlayerSerializer.base_fields['player'] = PlayerSerializer()

    class Meta:
        model = Player
        fields = ('id', 'username',)

class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        write_only_fields = ('password',) 
        fields = ('username', 'email', 'password')

    def validate_email(self, attrs, source):
        if not attrs['email']:
            raise serializers.ValidationError('The email field is required.')
        else:
            if Player.objects.filter(email = attrs[source]).exists():
                raise serializers.ValidationError('There is a user with the same email.')

        return attrs

    def restore_object(self, attrs, instance = None):
        # Retrieves
        if instance:
            instance.username = attrs.get('username', instance.username)
            instance.email = attrs.get('email', instance.email)
        # Creates
        else:
            request = self.context['request']
            if request.user.is_anonymous:
                instance = Player(email=attrs['email'], username=attrs['username'])
                instance.set_password(attrs['password'])

        return instance

class PlayerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('games',)
