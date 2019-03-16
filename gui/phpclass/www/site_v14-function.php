<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
      function sayHi($name) {
        echo "Hello User $name<br>";
      }
      function cube($num){
        return pow($num,3);
      }
      sayHi("Robinson");
      echo cube(4);
    ?>
  </body>
</html>
