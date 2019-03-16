<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="site_v10-url.php" method="post">
      Password: <input type="password" name="pwd"> <br>
      <input type="submit">
    </form>
      <?php
            $pwd = $_POST["pwd"];
            echo "I love you $pwd<br>";

      ?>
  </body>
</html>
