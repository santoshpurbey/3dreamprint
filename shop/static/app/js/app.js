'use strict';

angular.module('statumeApp', ['ngRoute', 'ngAnimate' ])

.config(function($routeProvider, $locationProvider){
  $routeProvider.when('/home',{
    controller: 'HomeController',
    templateUrl: '/static/app/views/home.html'
  }).otherwise('/');

  //$locationProvider.html5Mode(true);
})
.directive('slider', function ($timeout) {
  return {
    restrict: 'AE',
	replace: true,
	scope:{
		images: '='
	},
    link: function (scope, elem, attrs) {

		scope.currentIndex=0;

		scope.next=function(){
			scope.currentIndex<scope.images.length-1?scope.currentIndex++:scope.currentIndex=0;
		};

		scope.prev=function(){
			scope.currentIndex>0?scope.currentIndex--:scope.currentIndex=scope.images.length-1;
		};

		scope.$watch('currentIndex',function(){
			scope.images.forEach(function(image){
				image.visible=false;
			});
			scope.images[scope.currentIndex].visible=true;
		});

		/* Start: For Automatic slideshow*/

		var timer;

		var sliderFunc=function(){
			timer=$timeout(function(){
				scope.next();
				timer=$timeout(sliderFunc,3000);
			},3000);
		};

		sliderFunc();

		scope.$on('$destroy',function(){
			$timeout.cancel(timer);
		});

		/* End : For Automatic slideshow*/

    },
	//templateUrl:'views/templates/templateurl.html'
  }
})

/*slider products*/
.directive('productslider', function ($timeout) {
  return {
    restrict: 'AE',
	replace: true,
	scope:{
		products: '='
	},
    link: function (scope, elem, attrs) {

		scope.currentIndex=0;

		scope.next=function(){
			scope.currentIndex<scope.products.length-1?scope.currentIndex++:scope.currentIndex=0;
		};

		scope.prev=function(){
			scope.currentIndex>0?scope.currentIndex--:scope.currentIndex=scope.products.length-1;
		};

		scope.$watch('currentIndex',function(){
			scope.products.forEach(function(product){
				product.visible=false;
			});
			scope.products[scope.currentIndex].visible=true;
		});

		/* Start: For Automatic slideshow*/

		var timer;

		var sliderFunc=function(){
			timer=$timeout(function(){
				scope.next();
				timer=$timeout(sliderFunc,3000);
			},3000);
		};

		sliderFunc();

		scope.$on('$destroy',function(){
			$timeout.cancel(timer);
		});

		/* End : For Automatic slideshow*/

    },
	//templateUrl:'views/templates/templateurl.html'
  }
})
;
