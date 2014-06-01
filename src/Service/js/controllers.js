'use strict';

/* Controllers */

var trafficPath = "traffic.json";

angular.module('ORTServiceAPP.controllers', [])
  .controller('TrafficCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get(trafficPath).success(function(data) {
            $scope.data = data;
        });

  }])
  .controller('TrafficSingleCtrl', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams) {
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
  }])
  .controller('WeatherCtrl', ['$scope', function($scope) {

  }]);
