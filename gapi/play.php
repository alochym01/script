 <?php
//error_reporting(0);
require_once 'vendor/autoload.php';
require_once 'config.php';
require_once 'libs/curl.php';
require_once 'libs/gdrive.php';
require_once 'libs/gphotos.php';

$client = new Google_Client();
$client->setClientId(CLIENT_ID); //Google App's Client ID
$client->setClientSecret(CLIENT_SECRET); //Google App's Client secret
$client->setRedirectUri(AUTH_REDIRECT_URL); //Same Google App's Authorised redirect URIs
$client->setScopes(array('https://www.googleapis.com/auth/drive'));
$client->setAccessType ("offline");
$client->setApprovalPrompt ("force");

$output = "";
if(file_exists("./tokens/accesstoken.txt")) {
    $content = file_get_contents("./tokens/accesstoken.txt");
    $accessToken = json_decode($content, true) ;
    $client->setAccessToken($accessToken);
    if($client->isAccessTokenExpired()) {
        $currentAccessToken = $client->getAccessToken();
        $client->refreshToken($currentAccessToken['refresh_token']);
        $newAccessToken = $client->getAccessToken();
        $newAccessToken['refresh_token'] = $currentAccessToken['refresh_token'];
        file_put_contents("./tokens/accesstoken.txt", json_encode($newAccessToken));
        $accessToken = $currentAccessToken;
    }

    if($_GET && $_GET['url']){
        $url = $_GET['url'];
        $posGDrive = strpos($url, 'drive.google.com');
        $posDocs = strpos($url, 'docs.google.com');
        $posPhotos = strpos($url, 'photos.google.com');
        if($posGDrive !== false || $posDocs !== false){
            $output = get_google_drive($url, $accessToken['access_token']);
        }else if($posPhotos !== false){
            $output = get_google_photos($url);
        }
    }
} else {
    if(isset($_GET['code'])){
        $client->authenticate($_GET['code']);
        $accessToken = $client->getAccessToken();
        file_put_contents("./tokens/accesstoken.txt", json_encode($accessToken));
    }else{
        $authUrl = $client->createAuthUrl();
        header('Location: ' . $authUrl);
        exit();
    }
    $authUrl = $client->createAuthUrl();
}
?>
<?php if($output):?>
<?php 
    $md5url = md5($_GET['url']);
    $cachefile = './cached/'.$md5url;
    $cachetime = 3600;
    if (file_exists($cachefile) && time() - $cachetime < filemtime($cachefile)) {
        include($cachefile);
        exit;
    }
    ob_start();
?>
<div id="player"></div>
<script type="text/javascript" src="http://api.getlinkdrive.com/js/jwplayer/jwplayer.js"></script>
<script type="text/javascript">
    jwplayer.key = "rqQQ9nLfWs+4Fl37jqVWGp6N8e2Z0WldRIKhFg==";
    var playerInstance = jwplayer("player");
        playerInstance.setup({
            id:'player',
            sources: <?php echo $output; ?>,
            controls: true,
            displaytitle: true,
            width: "100%",
            height: "100%",
            aspectratio: "16:9",
            fullscreen: "true",
            autostart: true,
            abouttext: "Player for demo GetLinkDrive.com",
            aboutlink: "http://getlinkdrive.com/",
        });
</script>
<?php 
    $cached = fopen($cachefile, 'w');
    fwrite($cached, ob_get_contents());
    fclose($cached);
    ob_end_flush();
?>
<?php endif;?>