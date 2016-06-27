<?php
//if (isset($_POST['link'])) {
	$link = $_POST['link'];
    $link = 'https://drive.google.com/file/d/0B6xdFljd1ILaRlppTklyc3RBUWM/view?usp=sharing';
	$link = trim($link);
	$convertLink = convertLink($link);
	if(isset($convertLink['success'])){
		$return['success'] = '<b>Link here:</b><br />
							<span class="label label-success">Link View:</span> <a href="'.$convertLink["success"]["view"].'" target="_blank">'.$convertLink["success"]["view"].'</a><br />
							<span class="label label-success">Link Download:</span> <a href="'.$convertLink["success"]["download"].'" target="_blank">'.$convertLink["success"]["download"].'</a><br />
							';
		$video = '<h4 class="text-primary">Test Link For VideoJS Player</h4>
					<video id="my-video" class="video-js" controls preload="auto" width="600" height="340" poster="" data-setup="{}">
					    <source src="'.$convertLink["success"]["view"].'" type=\'video/mp4\'>
					    <p class="vjs-no-js">
					      To view this video please enable JavaScript, and consider upgrading to a web browser that
					      <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
					    </p>
					</video>
					<script src="http://vjs.zencdn.net/5.8.8/video.js"><\/script>';
		$return['video'] = $video;
	}else{
		$return['error'] = 1;
	}
	echo json_encode($return);
//}

function convertLink($link){
	if(preg_match('/.*drive.google.com\/.*\/(.*?)\/.*/is', $link, $id)){
		$result['success']['view'] = 'https://googledrive.com/host/'.$id[1];
		$result['success']['download'] = 'https://docs.google.com/uc?export=download&id='.$id[1];
	}else{
		$result['error'] = 'Link does not support';
	}
	return $result;
}

function getDriver($link)
{
	$get = curl($link);
	$data = explode('url_encoded_fmt_stream_map","', $get);
	$url = explode('"]', $data[1]);

	$url = str_replace(
		array('\u003d','\u0026'),
		array('=','&'),
		$url
	);
	$arrURL = explode('url=', $url[0]);
	$linkDownload = array();
	foreach ($arrURL as $key => $value) {
		if($key > 0){
			$urlDecoded = urldecode($value);
			//print_r($link); echo "<br>";
			preg_match('/\&itag\=(.*?)\&/', $urlDecoded, $itag);
			preg_match('/\&quality\=(.*?),/', $urlDecoded, $quality);
			preg_match('/\&quality\=(.*?)(.*)/', $urlDecoded, $quality2);
			if($quality[1])
				$qlt = $quality[1];
			else
				$qlt = $quality2[2];
			$linkDownload[$qlt.'-'.$itag[1]] = $urlDecoded;
		}
	}
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
