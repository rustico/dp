# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GamePlayer'
        db.create_table(u'games_gameplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Player'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.Game'])),
            ('player_invitation_status', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'games', ['GamePlayer'])

        # Adding field 'PlayerMatchPrediction.created_at'
        db.add_column(u'games_playermatchprediction', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 20, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PlayerMatchPrediction.updated_at'
        db.add_column(u'games_playermatchprediction', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 20, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Game.created_at'
        db.add_column(u'games_game', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 20, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Game.updated_at'
        db.add_column(u'games_game', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 20, 0, 0), blank=True),
                      keep_default=False)

        # Removing M2M table for field players on 'Game'
        db.delete_table(db.shorten_name(u'games_game_players'))


    def backwards(self, orm):
        # Deleting model 'GamePlayer'
        db.delete_table(u'games_gameplayer')

        # Deleting field 'PlayerMatchPrediction.created_at'
        db.delete_column(u'games_playermatchprediction', 'created_at')

        # Deleting field 'PlayerMatchPrediction.updated_at'
        db.delete_column(u'games_playermatchprediction', 'updated_at')

        # Deleting field 'Game.created_at'
        db.delete_column(u'games_game', 'created_at')

        # Deleting field 'Game.updated_at'
        db.delete_column(u'games_game', 'updated_at')

        # Adding M2M table for field players on 'Game'
        m2m_table_name = db.shorten_name(u'games_game_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'games.game'], null=False)),
            ('player', models.ForeignKey(orm[u'games.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'player_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'games.fixtureplayerpoints': {
            'Meta': {'object_name': 'FixturePlayerPoints'},
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Fixture']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Player']"}),
            'points': ('django.db.models.fields.IntegerField', [], {})
        },
        u'games.game': {
            'Meta': {'object_name': 'Game'},
            'classic': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner_games'", 'to': u"orm['games.Player']"}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'games'", 'symmetrical': 'False', 'through': u"orm['games.GamePlayer']", 'to': u"orm['games.Player']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'games.gameplayer': {
            'Meta': {'object_name': 'GamePlayer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Player']"}),
            'player_invitation_status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'games.player': {
            'Meta': {'object_name': 'Player'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['games.Player']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'games.playermatchprediction': {
            'Meta': {'object_name': 'PlayerMatchPrediction'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_double': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Player']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visitor_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'tournaments.fixture': {
            'Meta': {'ordering': "['number']", 'object_name': 'Fixture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'open_until': ('django.db.models.fields.DateTimeField', [], {}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        },
        u'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 20, 0, 0)'}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_classic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'local_team'", 'to': u"orm['tournaments.Team']"}),
            'local_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'suspended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visitor_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitor_team'", 'to': u"orm['tournaments.Team']"}),
            'visitor_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'tournaments.team': {
            'Meta': {'ordering': "['name']", 'object_name': 'Team'},
            'crest': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tournaments.tournament': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tournament'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['games']