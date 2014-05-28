'use strict';


// Declare app level module which depends on filters, and services
angular.module('ORTServiceAPP', [
  'ngRoute',
  'ORTServiceAPP.filters',
  'ORTServiceAPP.services',
  'ORTServiceAPP.directives',
  'ORTServiceAPP.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/start', {templateUrl: 'partials/start.html'});
  $routeProvider.when('/traffic', {templateUrl: 'partials/traffic_overview.html', controller: 'TrafficCtrl'});
  $routeProvider.when('/traffic/:id', {templateUrl: 'partials/traffic_detail.html', controller: 'TrafficSingleCtrl'});
  $routeProvider.when('/weather', {templateUrl: 'partials/weather.html', controller: 'WeatherCtrl'});
  $routeProvider.otherwise({redirectTo: '/start'});
}]);
