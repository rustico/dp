'use strict';
angular.module('app.games')

.factory('GameService', ['$http', 'SETTINGS', function($http, SETTINGS) {
    return {
        all: function(f_success, f_error) {
                $http.get(SETTINGS.url.games())
                    .success(function(response) {
                        console.log(response)

                        if(!!f_success) {
                            f_success(response);
                        }
                    })
                    .error(function(response) {
                        console.log(response);

                        if(!!f_error) {
                            f_success(response);
                        }
                    });
            },
        new: function(game, f_success, f_error) {
                $http.post(SETTINGS.url.newGame(), game)
                    .success(function(response) {
                        console.log(response)

                        if(!!f_success) {
                            f_success(response);
                        }
                    })
                    .error(function(response) {
                        console.log(response);

                        if(!!f_error) {
                            f_error(response);
                        }
                    });
        },
        get: function(game_id, f_success, f_error) {
                $http.get(SETTINGS.url.game(game_id))
                    .success(function(response) {
                        console.log(response)

                        if(!!f_success) {
                            f_success(response);
                        }
                    })
                    .error(function(response) {
                        console.log(response);

                        if(!!f_error) {
                            f_error(response);
                        }
                    });
        }
    }
}])

.factory('TournamentService', ['$http', function($http) {
    return {
        all: function(f_success, f_error) {
                $http.get('http://127.0.0.1:8000/tournaments/')
                    .success(function(response) {
                        console.log(response)

                        if(!!f_success) {
                            f_success(response);
                        }
                    })
                    .error(function(response) {
                        console.log(response);

                        if(!!f_error) {
                            f_error(response);
                        }
                    });
            }
    }
}]);
