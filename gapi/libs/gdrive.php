<?php
    function get_google_drive($url, $accessToken){
        $rurl = $url;
        $id1 = explode('open?id=',$rurl);
        if(empty($id1[1])){
            preg_match('/d\/(.*)\//U', $rurl, $id1);
        }if(empty($id1[1])){
            $id1[1] = $rurl;
        }
        $url = 'https://docs.google.com/get_video_info?docid='.$id1[1];
        $authorization = "Authorization: Bearer ".$accessToken;
        $get = curl_google($url, $authorization);
        $url_encoded_fmt_stream_map = $itag = $url = '';
        parse_str($get);
        $data = explode(',',$url_encoded_fmt_stream_map);
        $sources = array();
        foreach($data as $i => $format) {
            parse_str($format);
            $linkMp4    = preg_replace(["/[^\/]+\.googlevideo\.com/", "/ipbits=\d{2}/"], ["redirector.googlevideo.com", 'ipbits=0'], urldecode($url));
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