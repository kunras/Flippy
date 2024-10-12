<?php

require_once __DIR__ . "/../app/Router.php";

$router = new Router();

require_once __DIR__ . "/../app/Routes/web.php";

$router -> dispatch();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Coucou toi, tu es dans l'index</p>    
</body>
</html>