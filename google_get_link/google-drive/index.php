<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Demo Get Link Video Google Drive - BlogIT.vn</title>
	<meta name="description" content="Demo Tool Get Link Video Google Drive, code php get link video, file Google Drive."/>
	<meta property="og:title" content="Demo Tool Get Link Video Google Drive - BlogIT.vn" />
	<meta property="og:description" content="Demo Tool Get Link Video Google Drive by BlogIT.vn" />
	<meta property="og:image" content="http://blogit.vn/wp-content/uploads/2016/04/get-link-google-drive.jpg" />
	<meta property="og:url" content="http://demo.blogit.vn/google-drive" />
	<meta property="og:site_name" content="BlogIT.vn" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
	<link href="http://vjs.zencdn.net/5.8.8/video-js.css" rel="stylesheet">
  	<!-- If you'd like to support IE8 -->
  	<script src="http://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js"></script>
</head>
<body>
<div id="page-content">
    <div id="wrap">
        <div class="container">
			<div class="row">
				<div class="col-md-12">
					<h1>Demo Tool Get Link Video Google Drive</h1>
					<strong>View guide post <a target="_blank" href="#">here</a>.</strong>
					<div class="alert alert-dismissable alert-success">
						<strong>Link demo:</strong> https://drive.google.com/file/d/0B1xQLLJtrzJoaWUxUHdqY01mRGM/view
					</div>
					<form role="form" class="form-horizontal" id="form" method="post" onSubmit="return false;">  
						<div class="form-group">
						  <div class="col-md-12">
							<div class="input-group">
							  <input type="text" name="link" id="link" value="https://drive.google.com/file/d/0B1xQLLJtrzJoaWUxUHdqY01mRGM/view" class="form-control" autofocus>
							  <div class="input-group-btn">
								<button type="submit" id="submit" class="btn btn-info">Get Link</button>
							  </div>
							</div>
						  </div>
						</div>
					</form>
					<div id="listLink"></div>
					<div class="col-md-6 col-md-offset-3" id="demo"></div>
				</div>
			</div>
			<hr>
			<div class="col-md-12">
				<?php include('../list_tools.php'); ?>
			</div>
			<hr>
			<footer class="footer text-center">
			  <p>© <a target="_blank" href="http://blogit.vn">BlogIT.vn</a> 2015</p>
			</footer>
		</div>
	</div>
</div>
<script type="text/javascript">
$(document).ready(function(){
	$("#submit").click(function(){
		$("#submit").addClass('disabled');
		$("#listLink").html('<i class="fa fa-spinner fa-pulse"></i>');
		var form = $('#form')[0];
		var formData = new FormData(form);
		$.ajax({
			url: "get.php",
			type: "POST",
			data:  formData,
			contentType: false,
			cache: false,
			processData:false,
		  success: function(rs)
		  {
			res = JSON.parse(rs);
			if(res.success){
				$("#submit").removeClass('disabled');
				$("#listLink").html(res.success);
				$("#demo").html(res.video);
			}
			if(res.error){
				$("#submit").removeClass('disabled');
				$("#listLink").html('<b style="color:red">ERROR</b>');
			}
		  },
		  error: function() 
		  {
		  }           
		});
	});
});
</script>
</body>
</html>