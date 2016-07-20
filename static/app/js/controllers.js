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

        $scope.products=[
          {title:'Demo Product One', content:'Assault voodoo god paranoid tattoo modem kanji drone urban hotdog uplink computer. ', price: '55'},
          {title:'Demo Product Two', content:'Artisanal marketing RAF into advert geodesic sprawl realism woman dome footage courier table drone media youtube ablative', price: '52'},
          {title:'Demo Product Three', content:'Dome car papier-mache geodesic wonton soup RAF warehouse woman military-grade numinous shrine nodality pre. Physical drone chrome sunglasses footage vinyl disposable office denim youtube. Systemic-ware advert geodesic alcohol assassin monofilament shrine Chiba voodoo god film convenience store disposable industrial grade camera cartel.', price: '38'},
          {title:'Demo Product Four', content:'Assault voodoo god paranoid tattoo modem kanji drone urban hotdog uplink computer. ', price: '20'}
        ]
  }])
;
