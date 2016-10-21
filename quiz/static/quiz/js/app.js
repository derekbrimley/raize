$(function () {

	var progressBar = $("#progressbar"),
		progressLabel = $(".progress-label");

	var margin = (window.innerWidth-800)/2 - 10;

	$('.pageMargin').css('margin-left','-' + margin + 'px');
	$('.pageMargin').css('margin-right','-' + margin + 'px');
	$('.pageMargin').css('padding-top','5px');
	$('.pageMargin').css('padding-bottom','5px');

	progressBar.progressbar({
		value: 0,
		min: 0,
		max: 100,
		change: function() {
			progressLabel.text( progressBar.progressbar( "value" ) + "%" );
		}
	});

	$("#type_container").hide();
	$("#valuesContainer").hide();
	$("#interestsContainer").hide();
	$("#interestsContainer2").hide();
	$("#interestsContainer3").hide();
	$("#adjectivesContainer").hide();
	$("#personalityContainer").hide();
	$("#personalityContainer2").hide();
	$("#personalityContainer3").hide();
	$("#majorsContainer").hide();
	$("#friendsContainer").hide();
	$("#registrationContainer").hide();

	$( ".sortable" ).sortable();
    $( ".sortable" ).disableSelection();

	$( ".slider" ).labeledslider({
		min: 0,
		max: 10,
		value: 5,
		animate: "fast",
		tickArray: [0,1,2,3,4,5,6,7,8,9,10]
	})

	$(".valueSlider").labeledslider({
		min: 1,
		max: 7,
		value: 4,
		animate: "fast",
		tickArray: [1,2,3,4,5,6,7],
		tickLabels: {
			1: 'STRONGLY <br> DISAGREE',
			2: ' ',
			3: ' ',
			4: 'NEUTRAL',
			5: ' ',
			6: ' ',
			7: 'STRONGLY <br> AGREE'
		}
	});

	$(".personalitySlider").labeledslider({
		min: 0,
		max: 100,
		value: 50,
		step:10,
		animate: "fast",
		tickArray: [0,10,20,30,40,50,60,70,80,90,100],
	});

	$( ".check" ).button();

//	var majors = [
//		"Agriculture",
//		"Architecture",
//		"Arts",
//		"Biological Sciences",
//		"Business",
//		"Communications",
//		"Computer and Information",
//		"Sciences",
//		"Education",
//		"Engineering",
//		"Environmental Sciences",
//		"Health Care",
//		"Languages and Literature",
//		"Law",
//		"Mathematics",
//		"Mechanics",
//		"Military Science",
//		"Philosophy and Religion",
//		"Physical Sciences",
//		"Psychology and Counseling",
//		"Recreation and Fitness",
//		"Services",
//		"Skilled Trades and Contruction",
//		"Social Sciences and Liberal Arts",
//		"Social Services",
//		"Transportation"
//	];

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
	$("#id_value_6").val(5);
	$("#id_value_7").val(5);
	$("#id_value_8").val(5);
	$("#id_value_9").val(5);
	$("#id_value_10").val(5);

	$("#id_interest_1").val(false);
	$("#id_interest_2").val(false);
	$("#id_interest_3").val(false);
	$("#id_interest_4").val(false);
	$("#id_interest_5").val(false);
	$("#id_interest_6").val(false);
	$("#id_interest_7").val(false);
	$("#id_interest_8").val(false);
	$("#id_interest_9").val(false);
	$("#id_interest_10").val(false);
	$("#id_interest_11").val(false);
	$("#id_interest_12").val(false);
	$("#id_interest_13").val(false);
	$("#id_interest_14").val(false);
	$("#id_interest_15").val(false);
	$("#id_interest_16").val(false);
	$("#id_interest_17").val(false);
	$("#id_interest_18").val(false);

	$("#id_adjective_1").val(false);
	$("#id_adjective_2").val(false);
	$("#id_adjective_3").val(false);
	$("#id_adjective_4").val(false);
	$("#id_adjective_5").val(false);
	$("#id_adjective_6").val(false);
	$("#id_adjective_7").val(false);
	$("#id_adjective_8").val(false);
	$("#id_adjective_9").val(false);
	$("#id_adjective_10").val(false);
	$("#id_adjective_11").val(false);
	$("#id_adjective_12").val(false);

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

	$("#id_metric_11").val( 1 );
	$("#id_metric_12").val( 2 );
	$("#id_metric_13").val( 3 );
	$("#id_metric_14").val( 4 );
	$("#id_metric_15").val( 5 );
	$("#id_metric_16").val( 6 );
	$("#id_metric_17").val( 7 );
	$("#id_metric_18").val( 8 );


	$(".sortable").sortable({
		stop: function( event, ui){
			var order = $( "#sortablePersonality" ).sortable('toArray');

			$("#id_metric_11").val( order.indexOf("metric11") );
			$("#id_metric_12").val( order.indexOf("metric12") );
			$("#id_metric_13").val( order.indexOf("metric13") );
			$("#id_metric_14").val( order.indexOf("metric14") );
			$("#id_metric_15").val( order.indexOf("metric15") );
			$("#id_metric_16").val( order.indexOf("metric16") );
			$("#id_metric_17").val( order.indexOf("metric17") );
			$("#id_metric_18").val( order.indexOf("metric18") );
		}
	});
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

	$( "#value6Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_6").val( ui.value );
			value_6_value = ui.value;
		}
	});

	$( "#value7Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_7").val( ui.value );
			value_7_value = ui.value;
		}
	});

	$( "#value8Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_8").val( ui.value );
			value_8_value = ui.value;
		}
	});

	$( "#value9Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_9").val( ui.value );
			value_9_value = ui.value;
		}
	});

	$( "#value10Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_value_10").val( ui.value );
			value_10_value = ui.value;
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

	$('#interest6Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_6").val(true);
			interest_6_value = true;
		}else{
			$("#id_interest_6").val(false);
			interest_6_value = true;
		}
	});

	$('#interest7Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_7").val(true);
			interest_7_value = true;
		}else{
			$("#id_interest_7").val(false);
			interest_7_value = true;
		}
	});

	$('#interest8Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_8").val(true);
			interest_8_value = true;
		}else{
			$("#id_interest_8").val(false);
			interest_8_value = true;
		}
	});

	$('#interest9Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_9").val(true);
			interest_9_value = true;
		}else{
			$("#id_interest_9").val(false);
			interest_9_value = true;
		}
	});

	$('#interest10Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_10").val(true);
			interest_10_value = true;
		}else{
			$("#id_interest_10").val(false);
			interest_10_value = true;
		}
	});

	$('#interest11Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_11").val(true);
			interest_11_value = true;
		}else{
			$("#id_interest_11").val(false);
			interest_11_value = true;
		}
	});

	$('#interest12Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_12").val(true);
			interest_12_value = true;
		}else{
			$("#id_interest_12").val(false);
			interest_12_value = true;
		}
	});

	$('#interest13Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_13").val(true);
			interest_13_value = true;
		}else{
			$("#id_interest_13").val(false);
			interest_13_value = true;
		}
	});

	$('#interest14Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_14").val(true);
			interest_14_value = true;
		}else{
			$("#id_interest_14").val(false);
			interest_14_value = true;
		}
	});

	$('#interest15Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_15").val(true);
			interest_15_value = true;
		}else{
			$("#id_interest_15").val(false);
			interest_15_value = true;
		}
	});

	$('#interest16Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_16").val(true);
			interest_16_value = true;
		}else{
			$("#id_interest_16").val(false);
			interest_16_value = true;
		}
	});

	$('#interest17Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_17").val(true);
			interest_17_value = true;
		}else{
			$("#id_interest_17").val(false);
			interest_17_value = true;
		}
	});

	$('#interest18Checkbox').bind('change', function(){
		if($(this).is(':checked')){
			$("#id_interest_18").val(true);
			interest_18_value = true;
		}else{
			$("#id_interest_18").val(false);
			interest_18_value = true;
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

	$("#adjective6Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_6").val(true);
			adjective_6_value = true;
		}else{
			$("#id_adjective_6").val(false);
			adjective_6_value = true;
		}
	});

	$("#adjective7Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_7").val(true);
			adjective_7_value = true;
		}else{
			$("#id_adjective_7").val(false);
			adjective_7_value = true;
		}
	});

	$("#adjective8Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_8").val(true);
			adjective_8_value = true;
		}else{
			$("#id_adjective_8").val(false);
			adjective_8_value = true;
		}
	});

	$("#adjective9Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_9").val(true);
			adjective_9_value = true;
		}else{
			$("#id_adjective_9").val(false);
			adjective_9_value = true;
		}
	});

	$("#adjective10Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_10").val(true);
			adjective_10_value = true;
		}else{
			$("#id_adjective_10").val(false);
			adjective_10_value = true;
		}
	});

	$("#adjective11Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_11").val(true);
			adjective_11_value = true;
		}else{
			$("#id_adjective_11").val(false);
			adjective_11_value = true;
		}
	});

	$("#adjective12Checkbox").bind('change', function(){
		if($(this).is(':checked')){
			$("#id_adjective_12").val(true);
			adjective_12_value = true;
		}else{
			$("#id_adjective_12").val(false);
			adjective_12_value = true;
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

	$( "#personalityMetric11Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_11").val( ui.value );
			metric_11_value = ui.value;
		}
	});

	$( "#personalityMetric12Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_12").val( ui.value );
			metric_12_value = ui.value;
		}
	});

	$( "#personalityMetric13Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_13").val( ui.value );
			metric_13_value = ui.value;
		}
	});

	$( "#personalityMetric14Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_14").val( ui.value );
			metric_14_value = ui.value;
		}
	});

	$( "#personalityMetric15Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_15").val( ui.value );
			metric_15_value = ui.value;
		}
	});

	$( "#personalityMetric16Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_16").val( ui.value );
			metric_16_value = ui.value;
		}
	});

	$( "#personalityMetric17Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_17").val( ui.value );
			metric_17_value = ui.value;
		}
	});

	$( "#personalityMetric18Slider" ).labeledslider({
		change: function( event, ui ) {
			$("#id_metric_18").val( ui.value );
			metric_18_value = ui.value;
		}
	});

});//ready

//FORM VALUES

var value_1_value = '';
var value_2_value = '';
var value_3_value = '';
var value_4_value = '';
var value_5_value = '';
var value_6_value = '';
var value_7_value = '';
var value_8_value = '';
var value_9_value = '';
var value_10_value = '';

var interest_1_value = '';
var interest_2_value = '';
var interest_3_value = '';
var interest_4_value = '';
var interest_5_value = '';
var interest_6_value = '';
var interest_7_value = '';
var interest_8_value = '';
var interest_9_value = '';
var interest_10_value = '';
var interest_11_value = '';
var interest_12_value = '';
var interest_13_value = '';
var interest_14_value = '';
var interest_15_value = '';
var interest_16_value = '';
var interest_17_value = '';
var interest_18_value = '';

var adjective_1_value = '';
var adjective_2_value = '';
var adjective_3_value = '';
var adjective_4_value = '';
var adjective_5_value = '';
var adjective_6_value = '';
var adjective_7_value = '';
var adjective_8_value = '';
var adjective_9_value = '';
var adjective_10_value = '';
var adjective_11_value = '';
var adjective_12_value = '';

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
var metric_11_value = '';
var metric_12_value = '';
var metric_13_value = '';
var metric_14_value = '';
var metric_15_value = '';
var metric_16_value = '';
var metric_17_value = '';
var metric_18_value = '';

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
var email_6_value = '';
var email_7_value = '';
var email_8_value = '';
var email_9_value = '';
var email_10_value = '';

var first_name_value = '';
var last_name_value = '';
var email_value = '';
var password_value = '';
var password2_value = '';

//GLOBAL VARIABLES
var majorHtml = '';
var emailHtml = '';
var emailNum = 1;
var majorNum = 1;

var scrollToTop = function(){
	window.scrollTo(0,0);
}

var startQuiz = function(){

//	if($("#choiceBtnCollege").is(':checked') || $("#choiceBtnMajor").is(':checked') || $("#choiceBtnCompany").is(':checked')){
//		if($("#choiceBtnCollege").is(':checked')){
//
//		}else if($("#choiceBtnMajor").is(':checked')){
//
//		}else if($("#choiceBtnCompany").is(':checked')){
//
//		}
//		$("#homeContainer").hide();
//		$("#quizTitle").hide();
//
//		$("#valuesContainer").show();
//		scrollToTop();
//	}else{
//		alert("Please select an option.");
//	}
	$("#homeContainer").hide();
    $("#quizTitle").hide();

    $("#valuesContainer").show();
    scrollToTop();

	$("#progressbar").progressbar("value",12.5);
}

var goToInterests = function(){
	$("#valuesContainer").hide();

	$("#interestsContainer").show();
	scrollToTop();
	$("#progressbar").progressbar("value",25);
}
/*
var goToInterests2 = function(){
	$("#interestsContainer").hide();

	$("#interestsContainer2").show();
	scrollToTop();
	$("#progressbar").progressbar("value",30);
}

var goToInterests3 = function(){
	$("#interestsContainer2").hide();

	$("#interestsContainer3").show();
	scrollToTop();
	$("#progressbar").progressbar("value",40);
}
*/
var goToAdjectives = function(){
	if(!interest_1_value && !interest_2_value && !interest_3_value && !interest_4_value && !interest_5_value && !interest_6_value && !interest_7_value && !interest_8_value && !interest_9_value && !interest_10_value && !interest_11_value && !interest_12_value && !interest_13_value && !interest_14_value && !interest_15_value && !interest_16_value && !interest_17_value && !interest_18_value){
		alert("You must select at least one interest.");
		backToInterests();
	}
	else {
		$("#interestsContainer").hide();
		$("#adjectivesContainer").show();
		scrollToTop();
		$("#progressbar").progressbar("value",37.5);
	}

}

var goToPersonality = function(){
	if(!adjective_1_value && !adjective_2_value && !adjective_3_value && !adjective_4_value && !adjective_5_value && !adjective_6_value && !adjective_7_value && !adjective_8_value && !adjective_9_value && !adjective_10_value && !adjective_11_value && !adjective_12_value){
		alert("You must select two adjectives.");
		$("#registrationContainer").hide();
		$("#adjectivesContainer").show();
	}else if(adjective_1_value + adjective_2_value + adjective_3_value + adjective_4_value + adjective_5_value + adjective_6_value + adjective_7_value + adjective_8_value + adjective_9_value + adjective_10_value + adjective_11_value + adjective_12_value > 2){
		alert("You may only select two adjectives.");
		$("#registrationContainer").hide();
		$("#adjectivesContainer").show();
	}else {
		$("#adjectivesContainer").hide();
		$("#personalityContainer").show();
		scrollToTop();
		$("#progressbar").progressbar("value",50);
	}
}

var goToPersonality2 = function(){
	$("#personalityContainer").hide();

	$("#personalityContainer2").show();
	scrollToTop();
	$("#progressbar").progressbar("value",62.5);
}

var goToPersonality3 = function(){
	$("#personalityContainer2").hide();

	$("#personalityContainer3").show();
	scrollToTop();
	$("#progressbar").progressbar("value",75);
}

var goToMajors = function(){
	$("#personalityContainer3").hide();

	$("#registrationContainer").show();
	scrollToTop();
	$("#progressbar").progressbar("value",87.5);
}

//var goToFriends = function(){
//	$("#majorsContainer").hide();
//
//	$("#friendsContainer").show();
//	scrollToTop();
//}

//var goToRegistration = function(){
//	$("#majorsContainer").hide();
//
//	$("#registrationContainer").show();
//	scrollToTop();
//	$("#progressbar").progressbar("value",100);
//}

var goToEnd = function(){

}

var backToHome = function(){
	$("#valuesContainer").hide();
	$("#quizTitle").show();
	$("#homeContainer").show();
	scrollToTop();
    $("#progressbar").progressbar("value",0);
}

var backToValues = function(){
	$("#interestsContainer").hide();
	$("#valuesContainer").show();
	scrollToTop();
    $("#progressbar").progressbar("value",12.5);
}

var backToInterests = function(){
	$("#adjectivesContainer").hide();
	$("#interestsContainer").show();
	scrollToTop();
    $("#progressbar").progressbar("value",25);
}
/*
var backToInterests2 = function(){
	$("#interestsContainer3").hide();
	$("#interestsContainer2").show();
	scrollToTop();
    $("#progressbar").progressbar("value",30);
}

var backToInterests3 = function(){
	$("#adjectivesContainer").hide();
	$("#interestsContainer3").show();
	scrollToTop();
    $("#progressbar").progressbar("value",40);
}
*/
var backToAdjectives = function(){
	$("#personalityContainer").hide();
	$("#adjectivesContainer").show();
	scrollToTop();
    $("#progressbar").progressbar("value",37.5);
}

var backToPersonality = function(){
	$("#personalityContainer2").hide();
	$("#personalityContainer").show();
	scrollToTop();
    $("#progressbar").progressbar("value",50);
}

var backToPersonality2 = function(){
	$("#personalityContainer3").hide();
	$("#personalityContainer2").show();
	scrollToTop();
    $("#progressbar").progressbar("value",62.5);
}

//var backToPersonality3 = function(){
//	$("#majorsContainer").hide();
//	$("#personalityContainer3").show();
//	scrollToTop();
//}

var backToMajors = function(){
	$("#registrationContainer").hide();
	$("#personalityContainer3").show();
	scrollToTop();
    $("#progressbar").progressbar("value",75);
}

//var backToEmails = function(){
//	$("#registrationContainer").hide();
//	$("#friendsContainer").show();
//	scrollToTop();
//}

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

//var addEmailInput = function(){
//	if(emailNum == 1){
//		$("#id_email_3").prop('type', 'text');
//		$("#id_email_3").prop('placeholder', 'Email');
//	}else if (emailNum == 2){
//		$("#id_email_4").prop('type', 'text');
//		$("#id_email_4").prop('placeholder', 'Email');
//	}
//	else if (emailNum == 3){
//		$("#id_email_5").prop('type', 'text');
//		$("#id_email_5").prop('placeholder', 'Email');
//	}else{
//		alert("You can only send to five people.");
//	}
//	emailNum++;
//}

var submitQuiz = function(){

	first_name_value = $("#id_first_name").val();
	last_name_value = $("#id_last_name").val();
	email_value = $("#id_email").val();
	password_value = $("#id_password").val();
	password2_value = $("#id_password2").val();

	console.log("Last Name: " + last_name_value);
	console.log("Email: " + email_value);
	console.log("Password: " + password_value);
	console.log("Password 2: " + password2_value);

	console.log("Value 1: " + value_1_value);
	console.log("Value 2: " + value_2_value);
	console.log("Value 3: " + value_3_value);
	console.log("Value 4: " + value_4_value);
	console.log("Value 5: " + value_5_value);

	console.log("Interest 1: " + interest_1_value);
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

	console.log("Email 1: '" + email_1_value + "'");
	console.log("Email 2: " + email_2_value);
	console.log("Email 3: " + email_3_value);
	console.log("Email 4: " + email_4_value);
	console.log("Email 5: " + email_5_value);

	console.log("First Name: " + first_name_value);
	console.log("Last Name: " + last_name_value);
	console.log("Email: " + email_value);
	console.log("Password: " + password_value);
	console.log("Password 2: " + password2_value);

	/*
	if(!interest_1_value && !interest_2_value && !interest_3_value && !interest_4_value && !interest_5_value && !interest_6_value && !interest_7_value && !interest_8_value && !interest_9_value && !interest_10_value && !interest_11_value && !interest_12_value && !interest_13_value && !interest_14_value && !interest_15_value && !interest_16_value && !interest_17_value && !interest_18_value){
		alert("You must select at least one interest.");
		$("#registrationContainer").hide();
		$("#interestsContainer").show();
	}else  */


	if(!emailCheck(email_1_value) || !emailCheck(email_2_value) || !emailCheck(email_3_value) || !emailCheck(email_4_value) || !emailCheck(email_5_value)){
		alert("Invalid email!");
		$("#registrationContainer").hide();
		$("#friendsContainer").show();
	}else if(password_value != password2_value){
		alert("Passwords do not match!");
	}else if(first_name_value == '' || last_name_value == '' || email_value == '' || password_value == '' || password2_value == ''){
		alert("Please fill out your registration information to view your results.");
	}else if(!emailCheck(email_value)){
		alert("Invalid email!");
	}else{
		var dataString = $("#quiz_form").serialize();
		$("#quiz_form").submit();
//		$.ajax({
//			method: "POST",
//			url: '/quiz/submit/',
//			data: dataString,
//			statusCode: {
//				200: function(results){
//					$("#mainContainer").html(results);
//				}
//			}
//		});
	}
}

var submitFriendQuiz = function(){
	if(!interest_1_value && !interest_2_value && !interest_3_value && !interest_4_value && !interest_5_value && !interest_6_value && !interest_7_value && !interest_8_value && !interest_9_value && !interest_10_value && !interest_11_value && !interest_12_value && !interest_13_value && !interest_14_value && !interest_15_value && !interest_16_value && !interest_17_value && !interest_18_value){
		alert("You must select at least one interest.");
		$("#registrationContainer").hide();
		$("#interestsContainer").show();
	}else if(!adjective_1_value && !adjective_2_value && !adjective_3_value && !adjective_4_value && !adjective_5_value && !adjective_6_value && !adjective_7_value && !adjective_8_value && !adjective_9_value && !adjective_10_value && !adjective_11_value && !adjective_12_value){
		alert("You must select two adjectives.");
		$("#registrationContainer").hide();
		$("#adjectivesContainer").show();
	}else if(adjective_1_value + adjective_2_value + adjective_3_value + adjective_4_value + adjective_5_value + adjective_6_value + adjective_7_value + adjective_8_value + adjective_9_value + adjective_10_value + adjective_11_value + adjective_12_value > 2){
		alert("You may only select two adjectives.");
		$("#registrationContainer").hide();
		$("#adjectivesContainer").show();
	}
//    else if(major_1_value == ''){
//		alert("You must select at least one major.");
//		$("#registrationContainer").hide();
//		$("#majorsContainer").show();
//	}
    else{
		var user_id = $("#user_id").val();
		var dataString = $("#quiz_form").serialize();
		console.log(dataString);
		$("#quiz_form").submit();
//		$.ajax({
//			method: "POST",
//			url: '/quiz/'+user_id+'/friend_submit/',
//			data: dataString,
//			statusCode: {
//				200: function(results){
//					$("#mainContainer").html(results);
//				}
//			}
//		});
	}
}

var emailCheck = function(email){
	if(email == ''){
		return true;
	}else{
		var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    	return re.test(email);
	}
}
