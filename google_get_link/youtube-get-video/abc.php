<?php
//if (isset($_POST['link'])) {
$link = $_POST['link'];
    $link = 'https://www.youtube.com/watch?v=KjuGYC88CA8';
	$link = trim($link);
	$getVideoYoutube = getVideoYoutube($link);
	if ($getVideoYoutube) {
		$return['success'] = '<b>Link here:</b><br />';
		foreach($getVideoYoutube as $key => $linkDownload) {
			$return['success'].= '<span class="label label-success">' . $key . ':</span> <a href="' . $linkDownload . '" target="_blank"> click here</a><br />';
		}
	}
	else {
		$return['error'] = 1;
	}
	echo json_encode($return);
//}

function getIdYoutube($link){
    preg_match("#(?<=v=)[a-zA-Z0-9-]+(?=&)|(?<=v\/)[^&\n]+(?=\?)|(?<=v=)[^&\n]+|(?<=youtu.be/)[^&\n]+#", $link, $id);
    if(!empty($id)) {
        return $id = $id[0];
    }
	return $link;
}
function getVideoYoutube($id) {
	$id = getIdYoutube($id);
	$link = "https://www.youtube.com/watch?v=".$id;
	$get = curl($link);
	if ($get) {
		$return = array();
		if (preg_match('/;ytplayer\.config\s*=\s*({.*?});/', $get, $data)) {
			$jsonData  = json_decode($data[1], true);
            $streamMap = $jsonData['args']['url_encoded_fmt_stream_map'];
            foreach (explode(',', $streamMap) as $url)
            {
				$url = str_replace('\u0026', '&', $url);
                $url = urldecode($url);
                parse_str($url, $data);
                $dataURL = $data['url'];
                unset($data['url']);
                $return[$data['quality']."-".$data['itag']] = $dataURL.'&'.urldecode(http_build_query($data));
            }
        }
		return $return;
    }else{
    	return 0;
    }
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
