<?php
  // Get the code from the request
  $code = $_GET['code'];

  // Construct the path to the Internet shortcut file
  $filePath = "C:\\Users\\shacosta\\Desktop\\RockwellSearch\\MotionAnalyzer\\{$code}.url";

  // Open the file
  header('Content-Type: application/octet-stream');
  header("Content-Transfer-Encoding: Binary");
  header("Content-disposition: attachment; filename=\"" . basename($filePath) . "\"");
  readfile($filePath);
  exit;
?>
