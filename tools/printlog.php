<?php
$boughts = file("../db/boughts");
foreach ($boughts as $bought) {
	list($datestr, $ip, $pricetext, $product) = explode("\t", trim($bought));
	$date = strtotime($datestr);
	$price = floatval($pricetext);
	echo substr((date('d.H:i', $date) . " " . $price . " " . $product), 0, 24) . "\r\n";
}
?>
