<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
      $isMale = true;
      $isTall = true;
      if ($isMale && $isTall){
        echo "You are good candidate to play basketball";
      } else {
        echo "It's a girl";
      }
      if ($isMale || $isTall){
        echo "You are good candidate to play basketball";
      } elseif (!$isMale) {
        echo "It's a girl";
      }
    ?>
  </body>
</html>
