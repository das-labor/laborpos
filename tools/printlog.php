<?php
$boughts = file("../db/boughts");
$from = 277;

$descriptorspec = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w"),
   2 => array("pipe", "w")
);
$process = proc_open("python3 /home/pi/bonprint.py", $descriptorspec, $pipes);
if (is_resource($process)) {
	foreach ($boughts as $bought) {
		if ($from > 1)
		{
			--$from;
			continue;
		}
		list($datestr, $ip, $pricetext, $product) = explode("\t", trim($bought));
		$date = strtotime($datestr);
		$price = str_pad(number_format(floatval($pricetext), 2, ',', ''), 6, ' ', STR_PAD_LEFT);
		$printstr = substr((date('d.m. H:i', $date) . " " . $price . " €  " . $product), 0, 44) . "\r\n";
		echo $printstr;
		fwrite($pipes[0], $printstr);
	}
	fclose($pipes[0]);
	echo fread($pipes[1],1000);
	echo fread($pipes[2],1000);
	fclose($pipes[1]);
	proc_close($process);
}
?>
