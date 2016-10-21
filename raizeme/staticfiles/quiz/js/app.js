$(function(){
	$("#valuesContainer").hide();
	$("#interestsContainer").hide();
	$("#adjectivesContainer").hide();
	$("#personalityContainer").hide();
	$("#personalityContainer2").hide();
	$("#majorsContainer").hide();
	$("#friendsContainer").hide();
	$("#registrationContainer").hide();
	
	$( ".slider" ).labeledslider({
		min: 0,
		max: 10,
		value: 5,
		animate: "fast",
		tickArray: [0,1,2,3,4,5,6,7,8,9,10]
	})
	
	$(".personalitySlider").labeledslider({
		min: 0,
		max: 4,
		value: 2,
		animate: "fast",
		tickArray: [0,1,2,3,4],
		tickLabels: {
			0: 'Strongly Disagree',
			1: 'Disagree',
			2: 'Neither',
			3: 'Agree',
			4: 'Strongly Agree'
		}
	});
	
	$( ".check" ).button();
	
	var majors = [
		"Agriculture",
		"Architecture",
		"Arts",
		"Biological Sciences",
		"Business",
		"Communications",
		"Computer and Information",
		"Sciences",
		"Education",
		"Engineering",
		"Environmental Sciences",
		"Health Care",
		"Languages and Literature",
		"Law",
		"Mathematics",
		"Mechanics",
		"Military Science",
		"Philosophy and Religion",
		"Physical Sciences",
		"Psychology and Counseling",
		"Recreation and Fitness",
		"Services",
		"Skilled Trades and Contruction",
		"Social Sciences and Liberal Arts",
		"Social Services",
		"Transportation"
	];
	
	$("#majorInput").autocomplete({
		source: majors,
		change: function(event,ui){
			if (ui.item==null){
				$("#majorInput").val('');
				$("#majorInput").focus();
			}
        }
	});
	
	$("#id_value_1").val(5);
	$("#id_value_2").val(5);
	$("#id_value_3").val(5);
	$("#id_value_4").val(5);
	$("#id_value_5").val(5);
	
	$("#id_interest_1").val(false);
	$("#id_interest_2").val(false);
	$("#id_interest_3").val(false);
	$("#id_interest_4").val(false);
	$("#id_interest_5").val(false);
	
	$("#id_adjective_1").val(false);
	$("#id_adjective_2").val(false);
	$("#id_adjective_3").val(false);
	$("#id_adjective_4").val(false);
	$("#id_adjective_5").val(false);
	
	$("#id_metric_1").val( 2 );
	$("#id_metric_2").val( 2 );
	$("#id_metric_3").val( 2 );
	$("#id_metric_4").val( 2 );
	$("#id_metric_5").val( 2 );
	
	$("#id_metric_6").val( 2 );
	$("#id_metric_7").val( 2 );
	$("#id_metric_8").val( 2 );
	$("#id_metric_9").val( 2 );
	$("#id_metric_10").val( 2 );
	
	$( "#value1Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_1").val( ui.value );
			value_1_value = ui.value;
		}
	});
	
	$( "#value2Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_2").val( ui.value );
			value_2_value = ui.value;
		}
	});
	
	$( "#value3Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_3").val( ui.value );
			value_3_value = ui.value;
		}
	});
	
	$( "#value4Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_4").val( ui.value );
			value_4_value = ui.value;
		}
	});
	
	$( "#value5Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_5").val( ui.value );
			value_5_value = ui.value;
		}
	});
	
	$('#interest1Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_1").val(true);
			interest_1_value = true;
		}else{
			$("#id_interest_1").val(false);
			interest_1_value = false;
		}
	});
	
	$('#interest2Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_2").val(true);
			interest_2_value = true;
		}else{
			$("#id_interest_2").val(false);
			interest_2_value = true;
		}
	});
	
	$('#interest3Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_3").val(true);
			interest_3_value = true;
		}else{
			$("#id_interest_3").val(false);
			interest_3_value = true;
		}
	});
	
	$('#interest4Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_4").val(true);
			interest_4_value = true;
		}else{
			$("#id_interest_4").val(false);
			interest_4_value = true;
		}
	});
	
	$('#interest5Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_5").val(true);
			interest_5_value = true;
		}else{
			$("#id_interest_5").val(false);
			interest_5_value = true;
		}
	});
	
	$("#adjective1Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_1").val(true);
			adjective_1_value = true;
		}else{
			$("#id_adjective_1").val(false);
			adjective_1_value = true;
		}
	});
	
	$("#adjective2Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_2").val(true);
			adjective_2_value = true;
		}else{
			$("#id_adjective_2").val(false);
			adjective_2_value = true;
		}
	});
	
	$("#adjective3Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_3").val(true);
			adjective_3_value = true;
		}else{
			$("#id_adjective_3").val(false);
			adjective_3_value = true;
		}
	});
	
	$("#adjective4Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_4").val(true);
			adjective_4_value = true;
		}else{
			$("#id_adjective_4").val(false);
			adjective_4_value = true;
		}
	});
	
	$("#adjective5Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_5").val(true);
			adjective_5_value = true;
		}else{
			$("#id_adjective_5").val(false);
			adjective_5_value = true;
		}
	});
	
	$( "#personalityMetric1Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_1").val( ui.value );
			metric_2_value = ui.value;
		}
	});
	
	$( "#personalityMetric2Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_2").val( ui.value );
			metric_2_value = ui.value;
		}
	});
	
	$( "#personalityMetric3Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_3").val( ui.value );
			metric_3_value = ui.value;
		}
	});
	
	$( "#personalityMetric4Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_4").val( ui.value );
			metric_4_value = ui.value;
		}
	});
	
	$( "#personalityMetric5Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_5").val( ui.value );
			metric_5_value = ui.value;
		}
	});
	
	$( "#personalityMetric6Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_6").val( ui.value );
			metric_6_value = ui.value;
		}
	});
	
	$( "#personalityMetric7Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_7").val( ui.value );
			metric_7_value = ui.value;
		}
	});
	
	$( "#personalityMetric8Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_8").val( ui.value );
			metric_8_value = ui.value;
		}
	});
	
	$( "#personalityMetric9Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_9").val( ui.value );
			metric_9_value = ui.value;
		}
	});
	
	$( "#personalityMetric10Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_10").val( ui.value );
			metric_10_value = ui.value;
		}
	});
	
});//ready

//FORM VALUES
var value_1_value = '';
var value_2_value = '';
var value_3_value = '';
var value_4_value = '';
var value_5_value = '';

var interest_1_value = '';
var interest_2_value = '';
var interest_3_value = '';
var interest_4_value = '';
var interest_5_value = '';

var adjective_1_value = '';
var adjective_2_value = '';
var adjective_3_value = '';
var adjective_4_value = '';
var adjective_5_value = '';

var metric_1_value = '';
var metric_2_value = '';
var metric_3_value = '';
var metric_4_value = '';
var metric_5_value = '';

var metric_6_value = '';
var metric_7_value = '';
var metric_8_value = '';
var metric_9_value = '';
var metric_10_value = '';

var major_1_value = '';
var major_2_value = '';
var major_3_value = '';
var major_4_value = '';
var major_5_value = '';

var email_1_value = '';
var email_2_value = '';
var email_3_value = '';
var email_4_value = '';
var email_5_value = '';

var first_name_value = '';
var last_name_value = '';
var email_value = '';
var password_value = '';
var password_value = '';

//GLOBAL VARIABLES
var majorHtml = '';
var emailHtml = '';
var emailNum = 1;
var majorNum = 1;

var startQuiz = function(){
	$("#homeContainer").hide();

	$("#valuesContainer").show();
}

var goToInterests = function(){
	$("#valuesContainer").hide();

	$("#interestsContainer").show();
	
}

var goToAdjectives = function(){
	$("#interestsContainer").hide();
	
	$("#adjectivesContainer").show();
}

var goToPersonality = function(){
	$("#adjectivesContainer").hide();
	
	$("#personalityContainer").show();
}

var goToPersonality2 = function(){
	$("#personalityContainer").hide();
	
	$("#personalityContainer2").show();
}

var goToMajors = function(){
	$("#personalityContainer2").hide();
	
	$("#majorsContainer").show();
}

var goToFriends = function(){
	$("#majorsContainer").hide();
	
	$("#friendsContainer").show();
}

var goToRegistration = function(){
	$("#friendsContainer").hide();
	
	$("#registrationContainer").show();
}

var goToEnd = function(){
	
}

var backToHome = function(){
	$("#valuesContainer").hide();
	$("#homeContainer").show();
}

var backToValues = function(){
	$("#interestsContainer").hide();
	$("#valuesContainer").show();
}

var backToInterests = function(){
	$("#adjectivesContainer").hide();
	$("#interestsContainer").show();
}

var backToAdjectives = function(){
	$("#personalityContainer").hide();
	$("#adjectivesContainer").show();
}

var backToPersonality = function(){
	$("#personalityContainer2").hide();
	$("#personalityContainer").show();
}

var backToPersonality2 = function(){
	$("#majorsContainer").hide();
	$("#personalityContainer2").show();
}

var backToMajors = function(){
	$("#friendsContainer").hide();
	$("#majorsContainer").show();
}

var backToEmails = function(){
	$("#registrationContainer").hide();
	$("#friendsContainer").show();
}

var addMajor = function(){
	if(majorNum < 6){
		var major = $("#majorInput").val();
		if(major != ''){
			
			if(major != major_1_value && major != major_2_value && major != major_3_value && major != major_4_value && major != major_5_value){
				console.log("Major: " + major + " " + major_1_value);
				majorHtml += '<div class="majorItem" id="major'+majorNum+'">'+major+'</div>';
				$("#majorContainer").html(majorHtml);

				if(!($("#id_major_1").val().length)){
					$("#id_major_1").val(major);
					major_1_value = major;
				}else if(!($("#id_major_2").val().length)){
					$("#id_major_2").val(major);
					major_2_value = major;
				}else if(!($("#id_major_3").val().length)){
					$("#id_major_3").val(major);
					major_3_value = major;
				}else if(!($("#id_major_4").val().length)){
					$("#id_major_4").val(major);
					major_4_value = major;
				}else if(!($("#id_major_5").val().length)){
					$("#id_major_5").val(major);
					major_5_value = major;
				}
				majorNum++;	
			}else{
				alert("You already selected that major.");
			}
		}else{
			alert("You must select a major.")	
		}
		$("#majorInput").val('');
	}else{
		alert("You can only choose five majors.");
	}
}

var addEmailInput = function(){
	if(emailNum == 1){
		$("#id_email_3").prop('type', 'text');
		$("#id_email_3").prop('placeholder', 'Email');
	}else if (emailNum == 2){
		$("#id_email_4").prop('type', 'text');
		$("#id_email_4").prop('placeholder', 'Email');
	}
	else if (emailNum == 3){
		$("#id_email_5").prop('type', 'text');
		$("#id_email_5").prop('placeholder', 'Email');
	}else{
		alert("You can only send to five people.");
	}
	emailNum++;
}

var submitQuiz = function(){
	
	console.log("Value 1: " + value_1_value);
	console.log("Value 2: " + value_2_value);
	console.log("Value 3: " + value_3_value);
	console.log("Value 4: " + value_4_value);
	console.log("Value 5: " + value_5_value);
	
	console.log("Interest 1: " + value_1_value);
	console.log("Interest 2: " + interest_2_value);
	console.log("Interest 3: " + interest_3_value);
	console.log("Interest 4: " + interest_4_value);
	console.log("Interest 5: " + interest_5_value);
	
	console.log("Adjective 1: " + adjective_1_value);
	console.log("Adjective 2: " + adjective_2_value);
	console.log("Adjective 3: " + adjective_3_value);
	console.log("Adjective 4: " + adjective_4_value);
	console.log("Adjective 5: " + adjective_5_value);
	
	console.log("Metric 1: " + metric_1_value);
	console.log("Metric 2: " + metric_2_value);
	console.log("Metric 3: " + metric_3_value);
	console.log("Metric 4: " + metric_4_value);
	console.log("Metric 5: " + metric_5_value);
	
	console.log("Metric 6: " + metric_6_value);
	console.log("Metric 7: " + metric_7_value);
	console.log("Metric 8: " + metric_8_value);
	console.log("Metric 9: " + metric_9_value);
	console.log("Metric 10: " + metric_10_value);
	
	console.log("Major 1: " + major_1_value);
	console.log("Major 2: " + major_2_value);
	console.log("Major 3: " + major_3_value);
	console.log("Major 4: " + major_4_value);
	console.log("Major 5: " + major_5_value);
	
	console.log("Email 1: " + email_1_value);
	console.log("Email 2: " + email_2_value);
	console.log("Email 3: " + email_3_value);
	console.log("Email 4: " + email_4_value);
	console.log("Email 5: " + email_5_value);
	
	console.log("First Name: " + first_name_value);
	console.log("Last Name: " + last_name_value);
	console.log("Email: " + email_value);
	console.log("Password: " + password_value);
	console.log("Password 2: " + password_value);
	
	$("#quiz_form").submit();
}