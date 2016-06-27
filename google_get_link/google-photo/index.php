<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Demo Get Link Video Google Photo - BlogIT.vn</title>
	<meta name="description" content="Demo Tool Get Link Video Google Photo, code php get link video mp4 sd, hd, 360p, 480p, 720p, 1080p google photo."/>
	<meta property="og:title" content="Demo Tool Get Link Video Google Photo - BlogIT.vn" />
	<meta property="og:description" content="Demo Tool Get Link Video Google Photo by BlogIT.vn" />
	<meta property="og:image" content="http://blogit.vn/wp-content/uploads/2015/09/get-link-google-photo.jpg" />
	<meta property="og:url" content="http://demo.blogit.vn/google-photo" />
	<meta property="og:site_name" content="BlogIT.vn" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-66490881-1', 'auto');
  ga('send', 'pageview');

</script>
</head>
<body>
<div id="page-content">
    <div id="wrap">
        <div class="container">
			<div class="row">
				<div class="col-md-12">
					<h1>Demo Tool Get Link Video Google Photo</h1>
					<strong>Xem bài viết đầy đủ tại <a target="_blank" href="http://blogit.vn/huong-dan-get-link-video-google-photo-bang-curl.html">đây</a>.</strong>
					<div class="alert alert-dismissable alert-success">
						<strong>Link demo:</strong> https://photos.google.com/share/AF1QipNyYyBWbThLYpt6Pjqw5Y84UvDJL8QTSO9aCPW3nEOS7cXJEFJHpXELOZpb8VpdtA/photo/AF1QipNbBQXg9A60xLs1cLoivK1LIoQbtwJvzoRuI6Ar?key=Rmg0aE1BNkFsb0Z1VG9pUDVOYlRHT3JOb0xRejlR
					</div>
					<form role="form" class="form-horizontal" id="form" method="post" onSubmit="return false;">  
						<div class="form-group">
						  <div class="col-md-12">
							<div class="input-group">
							  <input type="text" name="link" id="link" value="https://photos.google.com/share/AF1QipNyYyBWbThLYpt6Pjqw5Y84UvDJL8QTSO9aCPW3nEOS7cXJEFJHpXELOZpb8VpdtA/photo/AF1QipNbBQXg9A60xLs1cLoivK1LIoQbtwJvzoRuI6Ar?key=Rmg0aE1BNkFsb0Z1VG9pUDVOYlRHT3JOb0xRejlR" class="form-control" autofocus>
							  <div class="input-group-btn">
								<button type="submit" id="submit" class="btn btn-info">Get Link</button>
							  </div>
							</div>
						  </div>
						</div>
					</form>
					<div id="listLink">
					</div>
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