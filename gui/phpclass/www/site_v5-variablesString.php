<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    $characterName = "Robinson";
    $characterAge = 50;

    echo strtolower($characterName);
    echo strtoupper($characterName);
    echo strlen($characterName);
    echo $characterName[0];
    echo "Exito 4 life"[0];
    echo "<br> He was $characterAge years old <br>";
    $characterName = "Milagros";
    echo $characterName[0] = "G";
    echo str_replace("ilag","iank", $characterName);
    echo substr($characterName, 3, 2);
    echo "He really liked the name $characterName <br>";
    echo "But didn't like being $characterAge <br>";
     ?>
  </body>
</html>
