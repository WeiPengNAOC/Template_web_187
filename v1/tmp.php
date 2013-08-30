<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>LAMOST Stellar Spectral Classfication Templates Library V1.0</title>
<link href="css/bootstrap.css" rel="stylesheet" media="screen">
<script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.js"></script>
</head>

<body>

 <div class="page-header">
  <h1>LAMOST Stellar Spectral Classfication Templates Library V1.0</h1>
</div>

<div class="navbar">



<ul class="breadcrumb">
  <li><a href="index.php">Home</a> <span class="divider">/</span></li>
  
</ul>
<div class="well">
<?php
$rid=intval($_REQUEST["id"]);
?>
<a href="tmp.php?id=<?php
echo $rid-1;
?>">-Pre-</a> 
 <a href="tmp.php?id=<?php
echo $rid+1;
?>">-Next-</a>
 <ul class="thumbnails"> 
<li class="span8">
    <div class="thumbnail">
 <img src="data/dr9_png/t_dr9_<?php 
echo str_pad($rid, 3, "0", STR_PAD_LEFT);
?>.png" alt="">
    
</a>
</div>
  </li>

<li class="span8">
    <div class="thumbnail">
 <img src="data/mk_png/t_mk_<?php 
echo str_pad($rid, 3, "0", STR_PAD_LEFT);
?>.png" alt="">
    
</a>
</div>
  </li>

</ul>

<a href="tmp.php?id=<?php
echo $rid-1;
?>">-Pre-</a> 
 <a href="tmp.php?id=<?php
echo $rid+1;
?>">-Next-</a>
</div>

  
</body>
</html>

