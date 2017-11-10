<?php
$f = fopen("db/boughts", "a") or die("Failed to open the database file");
$boughts = json_decode($_POST['data']);
$date = date('r');
$ip = $_SERVER['REMOTE_ADDR'];
foreach ($boughts as $bought) {
	fwrite($f, $date . "\t" . $ip . "\t" . $bought->price . "\t" . $bought->product . "\n");
}
fclose($f);
echo "OK";
?>