<?php
// Mendefinisikan direktori upload
$uploadDir = '/home/tajmahalfurnitur/public_html/';

// Cek jika ada file yang diupload
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Periksa apakah file telah di-upload dan tidak ada kesalahan
    if (isset($_FILES['fileToUpload']) && $_FILES['fileToUpload']['error'] == UPLOAD_ERR_OK) {
        $fileTmpName = $_FILES['fileToUpload']['tmp_name'];
        $fileName = basename($_FILES['fileToUpload']['name']);
        $uploadFilePath = $uploadDir . $fileName;

        // Verifikasi tipe file (opsional)
        $fileType = pathinfo($uploadFilePath, PATHINFO_EXTENSION);
        $allowedTypes = array('jpg', 'jpeg', 'png', 'gif', 'pdf'); // Tambahkan jenis file yang diizinkan

        if (in_array($fileType, $allowedTypes)) {
            // Pindahkan file dari direktori sementara ke direktori tujuan
            if (move_uploaded_file($fileTmpName, $uploadFilePath)) {
                $message = "File berhasil di-upload!";
            } else {
                $message = "Terjadi kesalahan saat memindahkan file.";
            }
        } else {
            $message = "Tipe file tidak diizinkan.";
        }
    } else {
        $message = "Tidak ada file yang di-upload atau terjadi kesalahan.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload File</title>
</head>
<body>
    <h1>Formulir Upload File</h1>

    <!-- Tampilkan pesan jika ada -->
    <?php if (isset($message)) : ?>
        <p><?php echo htmlspecialchars($message); ?></p>
    <?php endif; ?>

    <form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Pilih file untuk di-upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
