<?php

//if (isset($_POST['link'])) {
	$link = $_POST['link'];
	$link = 'https://photos.google.com/share/AF1QipNyYyBWbThLYpt6Pjqw5Y84UvDJL8QTSO9aCPW3nEOS7cXJEFJHpXELOZpb8VpdtA/photo/AF1QipNbBQXg9A60xLs1cLoivK1LIoQbtwJvzoRuI6Ar?key=Rmg0aE1BNkFsb0Z1VG9pUDVOYlRHT3JOb0xRejlR';
    $link = 'https://photos.google.com/share/AF1QipOURTsVJnhdrPPithrckA9ban6a78LZSvvsuT3F27aVH1WO-epzmBfYMOkvLP2T1w/photo/AF1QipOl9PR6ZBIh94lziQ7sot5xeAtImwh71vDzPTVZ?key=c3k1R2JFZGVKSjFTVW9aQ19PTzRjZjRBN1A4YW5R';
	$link = trim($link);
	$getPhotoGoogle = getPhotoGoogle($link);
	if ($getPhotoGoogle) {
		$return['success'] = '<b>Link here:</b><br />';
		foreach($getPhotoGoogle as $key => $linkDownload) {
			if ($key == '1080p') {
				$return['success'].= '<span class="label label-success">1080p:</span> <a href="' . $linkDownload . '" target="_blank">' . $linkDownload . '</a><br />';
			}

			if ($key == '720p') {
				$return['success'].= '<span class="label label-success">720p:</span> <a href="' . $linkDownload . '" target="_blank">' . $linkDownload . '</a><br />';
			}

			if ($key == '360p') {
				$return['success'].= '<span class="label label-success">360p:</span> <a href="' . $linkDownload . '" target="_blank">' . $linkDownload . '</a><br />';
			}
		}
	}
	else {
		$return['error'] = 1;
	}

	echo json_encode($return);
//}

function getPhotoGoogle($link)
{
	$get = curl($link);
	$data = explode('url\u003d', $get);
	$url = explode('%3Dm', $data[1]);
	$decode = urldecode($url[0]);
	$count = count($data);
	$linkDownload = array();
	if ($count > 4) {
		$v1080p = $decode . '=m37';
		$v720p = $decode . '=m22';
		$v360p = $decode . '=m18';
		$linkDownload['1080p'] = $v1080p;
		$linkDownload['720p'] = $v720p;
		$linkDownload['360p'] = $v360p;
	}

	if ($count > 3) {
		$v720p = $decode . '=m22';
		$v360p = $decode . '=m18';
		$linkDownload['720p'] = $v720p;
		$linkDownload['360p'] = $v360p;
	}

	if ($count > 2) {
		$v360p = $decode . '=m18';
		$linkDownload['360p'] = $v360p;
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
