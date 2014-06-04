'use strict';

/* Controllers */

var trafficPath = "traffic.json";
var weatherCurrentPath = "weatherCurrent.json";
var weatherForecastPath = "weatherForecast.json";

angular.module('ORTServiceAPP.controllers', [])
  .controller('TrafficCtrl', ['$scope', '$http', '$location', '$interval', function($scope, $http, $location, $interval) {
        $scope.loadData = function() {
            $http.get(trafficPath).success(function(data) {
                $scope.data = data;
                console.log('loaded');
            })};

        $scope.loadData();

        $scope.intervalLoader = $interval(function() {$scope.loadData()}, 30 * 1000);

        $scope.$on('$destroy', function() {
            console.log('close');
            $interval.cancel($scope.intervalLoader);
        });


        angular.element(window).on('keydown', function(event) {
            switch(event.keyCode)
            {
                case 97:
                    $location.path('/traffic').replace();
                    break;
                case 98:
                    $location.path('/weather').replace();
                    break;
                case 13:
                case 32:
                    $location.path('/traffic/0').replace();
                    break;
            }
            $scope.$apply();
        });
  }])
  .controller('TrafficSingleCtrl', ['$scope', '$http', '$routeParams', '$location', function($scope, $http, $routeParams, $location) {
        $scope.currentID = parseInt($routeParams.id);
        $scope.current = (parseInt($scope.currentID) + 1);

        $http.get(trafficPath).success(function(data) {
            $scope.data = data;
            $scope.currentData = $scope.data[$scope.currentID].fields;
            $scope.count = $scope.data.length;
            if($scope.hasNext())
            {
                $scope.nextData = $scope.data[$scope.currentID+1].fields;
            }
        });

        $scope.hasPrevious = function() {
            return $scope.current > 1;
        };

        $scope.hasNext = function() {
            return $scope.current < $scope.count;
        };

        angular.element(window).on('keydown', function(event) {
            switch(event.keyCode)
            {
                case 109:
                case 97:
                    $location.path('/traffic').replace();
                    break;
                case 98:
                    $location.path('/weather').replace();
                    break;
                case 13:
                case 32:
                case 40:
                    if($scope.hasNext())
                        $location.path('/traffic/'+($scope.currentID+1)).replace();
                    break;
                case 107:
                case 38:
                    if($scope.hasPrevious())
                        $location.path('/traffic/'+($scope.currentID-1)).replace();
                    break;
                default:
                    console.log(event.keyCode);
                    break;
            }
            $scope.$apply();
        });
  }])
  .controller('WeatherCtrl', ['$scope', '$http', '$location', '$interval', function($scope, $http, $location, $interval) {
        $scope.loadData = function() {
            $http.get(weatherCurrentPath).success(function(data) {
                $scope.currentData = data;
            });

            $http.get(weatherForecastPath).success(function(data) {
                $scope.forecastData = data.objects;
            });
        };

        $scope.loadData();

        $scope.intervalLoader = $interval(function() {$scope.loadData()}, 30 * 1000);

        $scope.$on('$destroy', function() {
            console.log('close');
            $interval.cancel($scope.intervalLoader);
        });

        angular.element(window).on('keydown', function(event) {
            switch(event.keyCode)
            {
                case 97:
                    $location.path('/traffic').replace();
                    break;
                case 98:
                    $location.path('/weather').replace();
                    break;
            }
            $scope.$apply();
        });
  }]);
