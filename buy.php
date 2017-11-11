<?php
$f = fopen("db/boughts", "a") or die("Failed to open the database file");
$boughts = json_decode($_POST['data']);
$date = date('r');
$ip = $_SERVER['REMOTE_ADDR'];
$printstr = "";
foreach ($boughts as $bought) {
	$product = html_entity_decode($bought->product);
	fwrite($f, $date . "\t" . $ip . "\t" . $bought->price . "\t" . $product . "\n");
	$printstr .= substr(date('d.H:i') . " " . $bought->price . " " . $product, 0, 24) . "\r\n";
}
fclose($f);
exec("echo \"".rtrim($printstr)."\\r\" | lpr -P bondrucker");
echo "OK";
?>
