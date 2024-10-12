<?php

class Router {
    private $routes = [];

    public function get($route, $callback) {
        $this -> addRoute("GET", $route, $callback);
    }

    public function post($route, $callback) {
        $this -> addRoute("POST", $route, $callback);
    }

    private function addRoute($method, $route, $callback) {
        $this -> routes[] = [
            "method" => $method,
            "route" => $route,
            "callback" => $callback
        ];
    }
    
    public function dispatch() {
        $requestedMethod = $_SERVER['REQUEST_METHOD'];
        $requestedUri = trim($_SERVER['REQUEST_URI'], '/');

        foreach ($this->routes as $route) {
            if ($route['method'] == $requestedMethod && trim($route['route'], '/') == $requestedUri) {
                call_user_func($route['callback']);
                return;
            }
        }
        
        // Si aucune route n'est trouvée
        echo "404 - Page not found";
    }
}