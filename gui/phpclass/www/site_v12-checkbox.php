<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="site_v12-checkbox.php" method="post">
      Apple  <input type="checkbox" name="fruit[]" value="apple"><br>
      Orange <input type="checkbox" name="fruit[]" value="orange"><br>
      Pear   <input type="checkbox" name="fruit[]" value="pear"><br>
      <input type="submit">
    </form>
    <?php
      $fruit = $_POST["fruit"];
    echo $fruit[0];
    echo count($fruit);
    ?>
  </body>
</html>
