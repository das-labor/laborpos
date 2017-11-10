<!DOCTYPE html>
<html lang="de">
	<head>
		<title>LaborPOS</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
		<link rel="stylesheet" href="css/style.css">
	</head>
	<body class="bg-dark">
		<div class="container-fluid">
			<div class="row">
				<div class="col-12 col-md-3 jumbotron fixed-top">
					<h1 id="price">0.00</h1>
					<div id="list"></div>
				</div>
				<div class="col-12 col-md-3" style="height: 400px"></div>
				<div class="col-12 col-md-9" id="products"><?php
$colors = ['primary', 'secondary', 'success', 'light', 'info', 'warning', 'danger'];
$products = file("db/products");
foreach ($products as $product) {
	list($colortext, $pricetext, $name) = explode("\t", trim($product));
	$color = intval($colortext);
	$price = floatval($pricetext);
	echo "
					<a href=\"#\" class=\"btn btn-sq-lg btn-" . $colors[$color] . "\">
						" . $name . "<br>" . number_format($price, 2) . "
					</a>";
}
?>
				</div>
				<div class="col-12" style="height:70px;"></div>
			</div>
		</div>

		<nav class="navbar fixed-bottom navbar-expand navbar-light bg-light justify-content-between">
			<ul class="navbar-nav mr-auto">
				<li class="nav-item mr-5">
					<a class="nav-link btn btn-lg btn-danger" href="#" id="clear" tabindex="1">Clear</a>
				</li>
				<li class="nav-item">
					<input class="mr-sm-2" type="text" placeholder="Custom Product" aria-label="Custom Product" id="customtext" tabindex="2">
					<input class="mr-sm-2" type="number" placeholder="1.00" aria-label="Price" id="customprice" style="width:60px" step="0.5" tabindex="3">
					<a class="btn btn-lg btn-primary" href="#" id="customadd" tabindex="4">Add</a>
				</li>
			</ul>
			<a class="btn btn-lg btn-success disabled" href="#" id="buy" tabindex="5">Buy</a>
		</nav>
		<script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
		<script src="js/main.js" type="text/javascript"></script>
		<audio id="sound" src="assets/cash.mp3" autostart="false"></audio>
	</body>
</html>