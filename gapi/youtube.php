<?php
    function get_google_youtube($urlYoutube, $accessToken){
        $rurl = $urlYoutube;
        $id1 = explode('watch?v=',$rurl);

        $url = 'http://www.youtube.com/get_video_info?&video_id=' . $id1[1];
        $authorization = "Authorization: Bearer ".$accessToken;
        $get = curl_google($url, $authorization);
        $thumbnail_url = $title = $url_encoded_fmt_stream_map = $type = $url = '';
	parse_str($get);
	
        $data = explode(',',$url_encoded_fmt_stream_map);    

        $sources = array();
        
        foreach($data as $i => $format) {
            $quality = $url = $itag ='';
	  
            parse_str($format);

            $linkMp4    = preg_replace(["/[^\/]+\.googlevideo\.com/"], ["redirector.googlevideo.com"], urldecode($url));
            
            if($itag == '18')
                $sources[]  = array('src' => $linkMp4, 'file' => $linkMp4, 'type' => 'mp4', 'label' => '360p', 'res' => '360p');
            if($itag == '59')
                $sources[]  = array('src' => $linkMp4, 'file' => $linkMp4, 'type' => 'mp4', 'label' => '480p', 'res' => '480p');
            if($itag == '22')
                $sources[]  = array('src' => $linkMp4, 'file' => $linkMp4, 'type' => 'mp4', 'label' => '720p', 'res' => '720p');
            if($itag == '37')
                $sources[]  = array('src' => $linkMp4, 'file' => $linkMp4, 'type' => 'mp4', 'label' => '1080p', 'res' => '1080p');
        }
        return json_encode($sources, JSON_UNESCAPED_SLASHES);
    }
?>