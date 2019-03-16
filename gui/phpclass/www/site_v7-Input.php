<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
      <form action="site_v7-Input.php" method="get">
        Name ...: <input type="text" name="inputName"> <br>
        Age ....: <input type="text" name="inputAge"><br>
        <input type="submit">
      </form>
      <br>
      Your name is ...: <?php echo $_GET["inputName"]?>
      <br>
      Your Age is ....: <?php echo $_GET["inputAge"]?>
      <br>
      Stoped at 1:15:41
  </body>
</html>
