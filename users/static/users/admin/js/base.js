$(function () {

	document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

	document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('.dropdown-trigger');
		var instances = M.Dropdown.init(elems, {hover:true});
	  });
		
	$(document).ready(function() {
    M.updateTextFields();
	});
	
	$(document).ready(function(){
    $('select').formSelect();
  });      
	$('.subnavbar').find ('li').each (function (i) {
	
		var mod = i % 3;
		
		if (mod === 2) {
			$(this).addClass ('subnavbar-open-right');
		}
		
	});
	
	
	
});