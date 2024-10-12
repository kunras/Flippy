<?php

namespace App\Controllers;

class HomeController {
    public function index() {
        return $this -> view("home");
    }

    public function comparateur() {
        return $this -> view("comparateur");
    }

    public function best_price() {
        return $this -> view("best_price");
    }
    
    public function listes() {
        return $this -> view("listes");
    }
    
    public function historique() {
        return $this -> view("historique");
    }
    
    public function faq() {
        return $this -> view("faq");
    }

    private function view($view, $data = []) {
        // Extraire les données pour les rendre disponibles dans la vue
        extract($data);

        // Inclure le fichier de la vue
        require __DIR__ . '\\..\\Views\\' . $view . '.php';
        echo "ceci est " . $view;
    }
}