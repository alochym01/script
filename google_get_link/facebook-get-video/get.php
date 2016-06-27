<?php
if (isset($_POST['link'])) {
	$link = $_POST['link'];
	$link = trim($link);
	$getVideoFacebook = getVideoFacebook($link);
	if ($getVideoFacebook) {
		$return['success'] = '<b>Link here:</b><br />';
		foreach($getVideoFacebook as $key => $linkDownload) {
			$return['success'].= '<span class="label label-success">' . $key . ':</span> <a href="' . $linkDownload . '" target="_blank">' . $linkDownload . '</a><br />';
		}
	}
	else {
		$return['error'] = 1;
	}
	echo json_encode($return);
}

function getVideoFacebook($link){
    if(substr($link, -1) != '/' && is_numeric(substr($link, -1))){
        $link = $link.'/';
    }
    preg_match('/https:\/\/www.facebook.com\/(.*)\/videos\/(.*)\/(.*)\/(.*)/U', $link, $id); // link dạng https://www.facebook.com/userName/videos/vb.IDuser/IDvideo/?type=2&theater
    if(isset($id[4])){
        $idVideo = $id[3];
    }else{
        preg_match('/https:\/\/www.facebook.com\/(.*)\/videos\/(.*)\/(.*)/U', $link, $id); // link dạng https://www.facebook.com/userName/videos/IDvideo
        if(isset($id[3])){
            $idVideo = $id[2];
        }else{
            preg_match('/https:\/\/www.facebook.com\/video\.php\?v\=(.*)/', $link, $id); // link dạng https://www.facebook.com/video.php?v=IDvideo
            $idVideo = $id[1];
            $idVideo = substr($idVideo, 0, -1);
        }
    }
    $embed = 'https://www.facebook.com/video/embed?video_id='.$idVideo; // đưa link về dạng embed
    $get = curl($embed);
    $data = explode('[["params","', $get); // tách chuỗi [["params"," thành mảng
    $data = explode('"],["', $data[1]); // tách chuỗi "],[" thành mảng
    $data = str_replace(
		array('\u00257B','\u00257D', '\u002522', '\u00253A', '\u00252C', '\u00255B', '\u00255D','\u00255C\u00252F', '\u00252F', '\u00253F', '\u00253D', '\u002526'),
		array('{', '}', '"', ':', ',', '[', ']','\/', '/', '?', '=', '&'),
		$data[0]
	); // thay thế các ký tự mã hóa thành ký tự đặc biệt
    $data = json_decode($data); // decode chuỗi
    $video_data = $data->video_data; // get video data
    $progressive = $video_data->progressive[0];
    $linkDownload = array();
    if(isset($progressive->hd_src)){
    	$linkDownload['HD'] = $progressive->hd_src;// link download HD
    }
    if(isset($progressive->sd_src)){
    	$linkDownload['SD'] = $progressive->sd_src;// link download SD
    }
    //$imageVideo = 'https://graph.facebook.com/'.$idVideo.'/picture'; // get ảnh thumbnail
    //$linkVideo = array_values($linkDownload);
    //$return['linkVideo'] = $linkVideo[0]; // link video có độ phân giải lớn nhất
    //$return['imageVideo'] = $imageVideo; // ảnh thumb của video
	//$return['linkDownload'] = $linkDownload; // link download video
    return $linkDownload;
}

function curl($url)
{
	$ch = @curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "Accept-Language: en-us,en;q=0.5";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(
		'Expect:'
	));
	$page = curl_exec($ch);
	curl_close($ch);
	return $page;
}

?>
