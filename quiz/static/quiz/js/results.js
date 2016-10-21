$(function(){
	$("#email_form_container").hide();
	$("#email_link_container").hide();
});//ready

var openEmailInputs = function(){
	$("#result_container").hide();
	$("#email_form_container").show();
}

var openEmailLink = function(){
	$("#result_container").hide();
	$("#email_link_container").show();
}

var submitEmails = function(){
	var data = $("#emailForm").serialize();
	var userId = $("#userId").val();
	
	if($("#id_email_1").val()==''){
		alert("You must write in at least one email.");
	}
	$.ajax({
		method: "POST",
		url: '/quiz/'+userId+'/send_emails/',
		data: data,
		statusCode: {
			200: function(results){
				$("#mainContainer").html(results);
			}
		}
	});
}