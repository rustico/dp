'use strict';
angular.module('app.predictions', [])

.config(['$routeProvider', function($routeProvider) {
      return $routeProvider
            .when('/predictions', { templateUrl: 'scripts/predictions/views/all.html' })
            .when('/pronosticos', { templateUrl: 'scripts/predictions/views/all.html' })
}])




