<?php 
function get_google_photos($url){
	$body = curl_google($url);
	$temp_array = explode('url\\u003d', $body);
	if(count($temp_array) > 2){
		$data_array = array(); $v360p = ''; $v720p = ''; $v1080p ='';
		$link = explode('%3Dm', $temp_array[1]);
	    $decode = urldecode($link[0]);
	    $count = count($temp_array);
	    if($count == 5) {
	        $v1080p = $decode . '=m37';
	        $v720p = $decode . '=m22';
	        $v360p = $decode . '=m18';
	        $data_array = array(
	            0 => array(
	            		"src" 		=> $v360p, 
	            		"file" 		=> $v360p, 
	            		"label" 	=> "360p", 
	            		"res"		=> "360p", 
	            		"type" 		=> "video/mp4"
	            	),
	            1 => array(
	            		"src" 		=> $v720p, 
	            		"file" 		=> $v720p, 
	            		"label" 	=> "720p", 
	            		"res"		=> "720p", 
	            		"type" 		=> "video/mp4"
	            	),
	            2 => array(
	            		"src" 		=> $v1080p, 
	            		"file" 		=> $v1080p, 
	            		"label" 	=> "1080p", 
	            		"res"		=> "1080p", 
	            		"type" 		=> "video/mp4"
	            	)
	            );
	    }else if($count == 4){
	        $v720p = $decode . '=m22';
	        $v360p = $decode . '=m18';
			$data_array = array(
	            0 => array(
	            		"src" 		=> $v360p, 
	            		"file" 		=> $v360p, 
	            		"label" 	=> "360p", 
	            		"res"		=> "360p", 
	            		"type" 		=> "video/mp4"
	            	),
	            1 => array(
	            		"src" 		=> $v720p, 
	            		"file" 		=> $v720p, 
	            		"label" 	=> "720p", 
	            		"res"		=> "720p", 
	            		"type" 		=> "video/mp4"
	            	)
	            );
	    }else if($count == 3){
	        $v360p = $decode . '=m18';
			$data_array = array(
	            0 => array(
	            		"src" 		=> $v360p, 
	            		"file" 		=> $v360p, 
	            		"label" 	=> "360p", 
	            		"res"		=> "360p", 
	            		"type" 		=> "video/mp4"
	            	)
	            );
	    }

	    return json_encode($data_array, JSON_UNESCAPED_SLASHES);
	}
}
