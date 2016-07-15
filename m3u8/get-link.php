<?php
include "curl.php";
include 'simple_html_dom.php';

function getLinkFilm($html, $filmId, $curl) {
    if (strpos($html, '-146')) {
        preg_match("/(\&token\=)(.*)(\",\"vplugin.host\")/",
            $html,
            $matches);
        $matches[2] = current(explode('","', $matches[2]));
        $token = current(explode(".split('", $matches[2]));
        $tokens = explode('-', $token);
        $token = $tokens[0];
        $time = $tokens[1];
        $urlDownload = "http://hdonline.vn/frontend/episode/xmlplay?ep=1&fid={$filmId}&token={$token}-{$time}&format=json&_x=0.8413578739490715";
    } else {
        preg_match("/(eval\(function\(p,a,c,k,e,d\)\{e)(.*)(split\(\'\|\'\)\,0\,\{\}\)\))/",
            $html,
            $matches);
        $htmlTokens = explode('|', $matches[0]);
        $token = null;
        $time = null;
        foreach ($htmlTokens as $htmlToken) {
            if (strlen($htmlToken) == 96 || strlen($htmlToken) == 86) {
                $token = $htmlToken;
            }

            if (strpos($htmlToken, '146') !== false) {
                $time = $htmlToken;
            }
        }

        if (!is_null($token) && !is_null($time)) {
            $urlDownload = "http://hdonline.vn/frontend/episode/xmlplay?ep=1&fid={$filmId}&token={$token}-{$time}&format=json&_x=0.8413578739490715";
        }
    }
    //var_dump($matches);
    return json_decode($curl->get($urlDownload), true);
}


$filmId = $argv[1];
$series = $argv[2];
$curl = new Curl();
$curl->get('http://hdonline.vn/');

$page = (int) ($series / 30) + 1;
$html = $curl->get("http://hdonline.vn/episode/ajax?film={$filmId}&episode=&page={$page}&search=");
$html = str_get_html($html);

$items = $html->find('a');

foreach ($items as $item) {
    if ($item->plaintext == $series) {
        $href = 'http://hdonline.vn' . $item->href;
        $htmlDetail = $curl->get($href);
        $data = getLinkFilm($htmlDetail, $filmId, $curl);
        if ($data) {
            die(json_encode($data));
        }
    }
}
