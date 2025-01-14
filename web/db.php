<?php
    session_start();

    header('Content-Type: text/html; charset=utf-8');

    $db = new mysqli('127.0.0.1', 'root', 'password', 'db name');
    $db->set_charset("utf8");

    function qr($query)
    {
        global $db;
        return $db->query($query);  //query()함수를 사용하여 데이터베이스에 테이블 생성
    }

?>



