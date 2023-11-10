list = [];

function generateList() {
	html = "";
	price = 0;
	for (item in list) {
		html += "<div class=\"row\"><div class=\"col-3\">" + list[item].price.toFixed(2) + "</div><div class=\"col-9\">" + list[item].product + "</div></div>";
		price += list[item].price;
	}
	$('#list').html(html);
	$('#price').text(price.toFixed(2));
}

function buy(method, sound) {	
	$.post("buy.py", {"method": method, "data": JSON.stringify(list)}, function(result){
		switch (result) {
			case 'OK':
			list = [];
			generateList();
			$(".action").addClass('disabled');
			$(sound)[0].currentTime = 0;
			$(sound)[0].play();
			break;

			default:
			alert("Error: " + result);
			break;
		}
	});
}

$(document).ready(function(){
	generateList();
	$("#products a").click(function(e){
		e.preventDefault();
		splits = $.trim($(this).html()).split("<br>");
		data = {'product': splits[0], 'price': parseFloat(splits[1])};
		list.push(data);
		generateList();
		$(".action").removeClass('disabled');
		$("#buy").focus();
	});
	$("#customadd").click(function(e){
		e.preventDefault();
		data = {'product': $("#customtext").val(), 'price': parseFloat($("#customprice").val())};
		list.push(data);
		generateList();
		$(".action").removeClass('disabled');
		$("#buy").focus();
	});
	$("#clear").click(function(e){
		e.preventDefault();
		list = [];
		generateList();
		$(".action").addClass('disabled');
	});
	$("#buy").click(function(e){
		e.preventDefault();
		buy(0, "#sound");
	});
	$("#buycash").click(function(e){
		e.preventDefault();
		buy(1, "#sound");
	});
	$("#buycard").click(function(e){
		e.preventDefault();
		buy(2, "#sound");
	});
	$("#undo").click(function(e){
		e.preventDefault();
		for (item in list) {
			list[item].price = -list[item].price;
		}
		buy(0, "#sound2");
	});
	$("#undocash").click(function(e){
		e.preventDefault();
		for (item in list) {
			list[item].price = -list[item].price;
		}
		buy(1, "#sound2");
	});
});
