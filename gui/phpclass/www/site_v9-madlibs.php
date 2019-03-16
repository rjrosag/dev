<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="site_v9-madlibs.php" method="get">
      Color: <input type="text" name="color"> <br>
      Plural noun: <input type="text" name="pluralNoun"><br>
      celebritry: <input type="text" name="celebrity"><br>
      <input type="submit">
    </form>
      <?php
            $color = $_GET["color"];
            $pluralNoun = $_GET["pluralNoun"];
            $celebrity = $_GET["celebrity"];
            echo "Roses are $color <br>";
            echo "$pluralNoun are blue<br>";
            echo "I love you $celebrity<br>";

      ?>
  </body>
</html>
