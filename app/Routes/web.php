<?php

use App\Controllers\HomeController;

$router -> get("/home", function() {
    $controller = new HomeController();
    $controller -> index();
});

$router -> get("/comparateur", function() {
    $controller = new HomeController();
    $controller -> comparateur();
});

$router -> get("/best_price", function() {
    $controller = new HomeController();
    $controller -> best_price();
});

$router -> get("/listes", function() {
    $controller = new HomeController();
    $controller -> listes();
});

$router -> get("/historique", function() {
    $controller = new HomeController();
    $controller -> historique();
});

$router -> get("/faq", function() {
    $controller = new HomeController();
    $controller -> faq();
});
