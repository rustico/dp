    // Generated by CoffeeScript 1.7.1
(function() {
  'use strict';
  angular.module('app', ['ngRoute', 'ngAnimate', 'ui.bootstrap', 'easypiechart', 'mgo-angular-wizard', 'textAngular', 'btford.socket-io', 'app.ui.ctrls', 'app.ui.directives', 'app.ui.services', 'app.controllers', 'app.directives', 'app.form.validation', 'app.ui.form.ctrls', 'app.ui.form.directives', 'app.tables', 'app.task', 'app.localization', 'app.chart.ctrls', 'app.chart.directives', 'app.core', 'app.users', 'app.home', 'app.games', 'app.friends', 'app.predictions', 'app.notifications', 'app.contact']).config([
    '$routeProvider', function($routeProvider) {
      return $routeProvider.when('/ui/typography', {
        templateUrl: 'views/ui/typography.html'
      }).when('/ui/buttons', {
        templateUrl: 'views/ui/buttons.html'
      }).when('/ui/icons', {
        templateUrl: 'views/ui/icons.html'
      }).when('/ui/grids', {
        templateUrl: 'views/ui/grids.html'
      }).when('/ui/widgets', {
        templateUrl: 'views/ui/widgets.html'
      }).when('/ui/components', {
        templateUrl: 'views/ui/components.html'
      }).when('/ui/timeline', {
        templateUrl: 'views/ui/timeline.html'
      }).when('/forms/elements', {
        templateUrl: 'views/forms/elements.html'
      }).when('/forms/layouts', {
        templateUrl: 'views/forms/layouts.html'
      }).when('/forms/validation', {
        templateUrl: 'views/forms/validation.html'
      }).when('/forms/wizard', {
        templateUrl: 'views/forms/wizard.html'
      }).when('/tables/static', {
        templateUrl: 'views/tables/static.html'
      }).when('/tables/responsive', {
        templateUrl: 'views/tables/responsive.html'
      }).when('/tables/dynamic', {
        templateUrl: 'views/tables/dynamic.html'
      }).when('/charts/others', {
        templateUrl: 'views/charts/charts.html'
      }).when('/charts/morris', {
        templateUrl: 'views/charts/morris.html'
      }).when('/charts/flot', {
        templateUrl: 'views/charts/flot.html'
      }).when('/mail/inbox', {
        templateUrl: 'views/mail/inbox.html'
      }).when('/mail/compose', {
        templateUrl: 'views/mail/compose.html'
      }).when('/mail/single', {
        templateUrl: 'views/mail/single.html'
      }).when('/pages/features', {
        templateUrl: 'views/pages/features.html'
      }).when('/pages/signin', {
        templateUrl: 'views/pages/signin.html'
      }).when('/pages/signup', {
        templateUrl: 'views/pages/signup.html'
      }).when('/pages/lock-screen', {
        templateUrl: 'views/pages/lock-screen.html'
      }).when('/pages/profile', {
        templateUrl: 'views/pages/profile.html'
      }).when('/404', {
        templateUrl: 'views/pages/404.html'
      }).when('/pages/500', {
        templateUrl: 'views/pages/500.html'
      }).when('/pages/blank', {
        templateUrl: 'views/pages/blank.html'
      }).when('/pages/invoice', {
        templateUrl: 'views/pages/invoice.html'
      }).when('/tasks', {
        templateUrl: 'views/tasks/tasks.html'
      }).otherwise({
        redirectTo: '/404'
      });
    }
  ])
      
.constant('SETTINGS', {
    url : { base: 'http://127.0.0.1:8000',
            auth: function() { return this.base + '/api-token-auth/' },
            social_auth: function(backend) { return this.base + '/games/sociallogin/' + backend },
            player: function() { return this.base + '/games/player/' } ,
            playerFriends: function() { return this.base + '/games/player/friends' },
            playerSearch: function(username) { return this.base + '/games/players/search/' + username + '/'},
            playerMakeFriend: function() { return this.base + '/games/player/friend'},
            playerUpdateFriendship: function(player_id) { return this.base + '/games/player/friend/' + player_id + '/'},
            newGame: function() { return this.base + '/games/' },
            games: function() { return this.base + '/games/list/' },
            game: function(id) { return this.base + '/games/' + id + '/' },
            gamePlayerStatus: function(gameplayer_id) { return this.base + '/games/gameplayer/' + gameplayer_id + '/'},
            gamePlayerInviteAgain : function(gameplayer_id) { return this.base + '/games/gameplayer/invites-again/' + gameplayer_id + '/'},
            gamePlayerAnotherChance: function(gameplayer_id) { return this.base + '/games/gameplayer/another-chance/' + gameplayer_id + '/'},
            gamePlayerCreate: function() { return this.base + '/games/gameplayer/' },
            doPrediction: function() { return this.base + '/games/prediction/'},
            getPredictions: function(gameplayer_id) { return this.base + '/games/predictions/' + gameplayer_id + '/' },
            updateNotification: function(pk, notification_type) { return this.base + '/notifications/' + pk + '/' + notification_type },
            contactNew: function() { return this.base + '/contact/'},
            allTournamentsHomepage: function() { return this.base + '/homepage/tournaments'},            
            allTournaments: function() { return this.base + '/tournaments/'},
            allTournamentsNextFixture: function() { return this.base + '/tournaments/fixtures/next'},
            allTournamentsCurrentOrLastFixture: function() { return this.base + '/tournaments/fixtures/current-or-last'}, 
            tournamentFixture: function(tournament_id) { return this.base + '/tournaments/' + tournament_id + '/fixture' },
            tournamentStats: function(tournament_id) { return this.base + '/tournaments/' + tournament_id + '/stats' },
            allNews: function() { return this.base + '/homepage/news'}
    }
}) 

.factory('Data', [function () { return {} ; }])

.run(function ($rootScope, $location, AuthenticationService) {
    $rootScope.$on("$routeChangeStart", function(event, next, current){
	console.info(next);
        if (next.authenticate && !AuthenticationService.isAuthenticated()){
            $location.path( "/signin" );
            event.preventDefault(); 
        }

	var go_to_homepage = next.$$route.originalPath.indexOf('bienvenido') > 0 || 
	    (!!next.$$route.redirectTo && next.$$route.redirectTo.indexOf('bienvenido')) > 0;
	    
	if (AuthenticationService.isAuthenticated() && go_to_homepage ){
	    console.info("hola");
            $location.path( "/noticias" );
            event.preventDefault(); 
        }
    });
});

}).call(this);
