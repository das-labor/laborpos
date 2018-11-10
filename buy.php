<?php
$f = fopen("db/boughts", "a") or die("Failed to open the database file");
$boughts = json_decode($_POST['data']);
$date = date('r');
$ip = $_SERVER['REMOTE_ADDR'];
$printstr = "";
foreach ($boughts as $bought) {
	$product = html_entity_decode($bought->product);
	fwrite($f, $date . "\t" . $ip . "\t" . $bought->price . "\t" . $product . "\n");
	
	$datet = strtotime($date);
	$price = str_pad(number_format(floatval($bought->price), 2, ',', ''), 6, ' ', STR_PAD_LEFT);
	$printstr .= substr((date('d.m. H:i', $datet) . " " . $price . " €  " . $product), 0, 44) . "\r\n";
}
fclose($f);
//exec("echo \"".rtrim($printstr)."\\r\" | lpr -P bondrucker");

$descriptorspec = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w")
);
$process = proc_open("python3 /home/pi/bonprint.py", $descriptorspec, $pipes);
if (is_resource($process)) {
    fwrite($pipes[0], utf8_decode($printstr));
    fclose($pipes[0]);
    fclose($pipes[1]);
    proc_close($process);
}
echo "OK";
?>
