<?php

  error_reporting(E_ALL);
  ini_set('display_errors', 1);

  // Get the code from the request
  $code = $_GET['code'];

  // Construct the path to the Internet shortcut file
  $filePath = "C:\\Users\\shacosta\\Desktop\\RockwellSearch\\MotionAnalyzer\\{$code}.url";
  // Check if the file exists
  if (file_exists($filePath)) {
    // Return a response indicating that the file was found
    echo json_encode(array("found" => true));
  } else {
    // Return a response indicating that the file was not found
    echo json_encode(array("found" => false));
  }
?>