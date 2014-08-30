from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Player, FixturePlayerPoints
from tournaments.models import Fixture

@receiver(post_save, sender=Player)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Fixture)
def calculate_fixture_points(sender, instance=None, created=False, **kwargs):
    if instance.is_finished:
        for game in instance.tournament.game_set.all(): # This could take like an insane mount of time
            for gameplayer in game.gameplayer_set.filter(status = True):
                points = gameplayer.get_fixture_points(instance)

                try:
                  fp = FixturePlayerPoints.objects.get(fixture = instance, gameplayer = gameplayer)
                  fp.points = points

                except FixturePlayerPoints.DoesNotExist as e:
                  fp = FixturePlayerPoints(fixture = instance, gameplayer = gameplayer, points = points)

                fp.save()
