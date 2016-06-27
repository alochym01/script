<?php
if (isset($_POST['link'])) {
	$link = $_POST['link'];
	$link = trim($link);
	$getPicasaGoogle = getPicasaGoogle($link);
	if ($getPicasaGoogle) {
		$return['success'] = '<b>Link here:</b><br />';
		foreach($getPicasaGoogle as $key => $linkDownload) {
			$return['success'].= '<span class="label label-success">' . $key . ':</span> <a href="' . $linkDownload . '" target="_blank">' . $linkDownload . '</a><br />';
		}
	}
	else {
		$return['error'] = 1;
	}
	echo json_encode($return);
}

function getPicasaGoogle($link)
{
	$get = curl($link);
	$data = explode('"media":{"content":[', $get);
	$data2 = explode('],"', $data[1]);
	$data3 = explode('},', $data2[0]);
	$links = array();
	foreach($data3 as $value) {
		$value = str_replace("}}", "}", $value . "}");
		$links[] = json_decode($value, true);
	}

	$linkDownload = array();
	foreach($links as $k => $v) {
		if ($v['type'] == 'video/mpeg4') {
			$quality = $v['height'];
			$linkDownload[$quality] = $v['url'];
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

function getDirectLink($url)
{
	$urlInfo = parse_url($url);
	$out = "GET  {$url} HTTP/1.1\r\n";
	$out.= "Host: {$urlInfo['host']}\r\n";
	$out.= "User-Agent: {$_SERVER['HTTP_USER_AGENT']}\r\n";
	$out.= "Connection: Close\r\n\r\n";
	$con = @fsockopen('ssl://' . $urlInfo['host'], 443, $errno, $errstr, 10);
	if (!$con) {
		return $errstr . " " . $errno;
	}

	fwrite($con, $out);
	$data = '';
	while (!feof($con)) {
		$data.= fgets($con, 512);
	}

	fclose($con);
	preg_match("!\r\n(?:Location|URI): *(.*?) *\r\n!", $data, $matches);
	$url = $matches[1];
	return trim($url);
}
?>