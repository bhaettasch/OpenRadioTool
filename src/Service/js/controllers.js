'use strict';

/* Controllers */

var trafficPath = "traffic.json";
var weatherCurrentPath = "weatherCurrent.json";
var weatherForecastPath = "weatherForecast.json";

angular.module('ORTServiceAPP.controllers', [])
  .controller('TrafficCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
        $http.get(trafficPath).success(function(data) {
            $scope.data = data;
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
  .controller('WeatherCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
        $http.get(weatherCurrentPath).success(function(data) {
            $scope.currentData = data;
        });

        $http.get(weatherForecastPath).success(function(data) {
            $scope.forecastData = data.objects;
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
