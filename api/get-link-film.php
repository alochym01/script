<?php
include "curl.php";
include 'simple_html_dom.php';
// php /path/to/www/public/path/to/script.php filmId token

function getLinkFilm($token, $filmId, $curl) {
        $urlDownload = "http://hdonline.vn/frontend/episode/xmlplay?ep=1&fid={$filmId}&token={$token}&format=json&_x=0.8413578739490715";
    return json_decode($curl->get($urlDownload), true);
}

$curl = new Curl();
$curl->get('http://hdonline.vn/');

$filmId = $argv[1];
$token = $argv[2];
$data = getLinkFilm($token, $filmId, $curl);
if ($data) {
    die(json_encode($data));
}
die(json_encode(array()));
