var todoApp = angular.module("todoApp",[]);

todoApp.config([
                '$httpProvider',
                '$interpolateProvider',
                function($httpProvider, $interpolateProvider, $resourceProvider) {
                    $interpolateProvider.startSymbol('[[');
                    $interpolateProvider.endSymbol(']]');
                    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
                    $httpProvider.defaults.transformRequest = function(data){
                        if (data === undefined) {
                            return data;
                        }
                        return $.param(data);
                    };
                }
            ]);
var model = {
                user : "반상현",
                items: [{ action: "꽃사기", done: false},
                    { action: "신발사기", done: true},
                    { action: "티켓모으기", done: false},
                ]
            };
            


    todoApp.controller("ToDoCtrl", function($scope){
        $scope.todo = model;

        $scope.incomplimentCount = function () {
            var count = 0;
            angular.forEach($scope.todo.items, function (item) {
                if(!item.done){ count++}
            });
            return count;
        }

        $scope.warningLevel = function () {
            return $scope.incomplimentCount() <3 ? "label-success" : "label-worning";
        }

        $scope.addNewItem = function (actionText) {
            $scope.todo.items.push({action: actionText, done: false});
        }
    });

    todoApp.run(function ($http) {
        $http.get('/static/json/todo.json').success(function (data) {
            model.items = data;
        });
    });

