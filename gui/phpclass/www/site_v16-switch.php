<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
      $fruit = "orange";
      switch ($fruit){
        case "apple":
          echo "Today your fruit is Apple";
          break;
        case "orange":
            echo "Today your fruit is orange";
            break;
        default:
            echo "Sorry no fruit for today...";
              break;
      }
    ?>
  </body>
</html>
