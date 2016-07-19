'use strict';

angular.module('statumeApp')
  .controller('HomeController',['$scope', function($scope){
      console.log("Inside HomeController");
      $scope.images=[
        {src:'cup1.jpg',title:'Pic 1'},
        {src:'cup2.jpg',title:'Pic 2'},
        {src:'cup3.jpg',title:'Pic 3'},
        {src:'cup4.jpg',title:'Pic 4'},
        {src:'img5.png',title:'Pic 5'}];

  }])
;
