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

    private function view($view) {
        // Extraire les données pour les rendre disponibles dans la vue
        // extract($data);

        // Construire le chemin de la vue
        $viewFile = __DIR__ . '\\..\\Views\\' . $view . '.php';

        // Vérifier si le fichier existe
        if (file_exists($viewFile)) {
            // Inclure la vue si elle existe
            require $viewFile;
        } else {
            // Gérer l'erreur si la vue n'existe pas
            echo "La vue {$view} n'existe pas.";
        }
    }
}