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

$(document).ready(function(){
	generateList();
	$("#products a").click(function(e){
		e.preventDefault();
		splits = $.trim($(this).html()).split("<br>");
		data = {'product': splits[0], 'price': parseFloat(splits[1])};
		list.push(data);
		generateList();
		$("#buy").removeClass('disabled');
		$("#buy").focus();
	});
	$("#customadd").click(function(e){
		e.preventDefault();
		data = {'product': $("#customtext").val(), 'price': parseFloat($("#customprice").val())};
		list.push(data);
		generateList();
		$("#buy").removeClass('disabled');
		$("#buy").focus();
	});
	$("#clear").click(function(e){
		e.preventDefault();
		list = [];
		generateList();
		$("#buy").addClass('disabled');
	});
	$("#buy").click(function(e){
		e.preventDefault();
		$.post("buy.php", {"data": JSON.stringify(list)}, function(result){
			switch (result) {
				case 'OK':
				list = [];
				generateList();
				$("#buy").addClass('disabled');
				$("#sound")[0].currentTime = 0;
				$("#sound")[0].play();
				break;

				default:
				alert("Error: " + result);
				break;
			}
		});
	});
});