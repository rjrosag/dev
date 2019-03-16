<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="site_v13-AVP.php" method="post">
      Student name:  <input type="text" name="student"><br>
      <input type="submit">
    </form>
    <?php
      $grade = $arrayName = array('Jim' =>"A" , "David" => "A", "Daniel" => "C" );
      echo $grade[$_POST["student"]];
    echo count($grade);
    ?>
  </body>
</html>
