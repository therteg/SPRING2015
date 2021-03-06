$(document).ready(function() {

	// waypoints for text show effect 

	        $('.container').waypoint(function(direction){
	        	if ('down' === direction){
	        		$('.quote').removeClass('text').addClass('show');
	        	} 
	        }, { offset: '-70%' });

	        if (document.body.clientWidth>500){
	        	
	        	$('footer').waypoint(function(direction){
	        	if ('down' === direction){
	        		$('footer .container').removeClass('text').addClass('show');
	        	}
	        	}, { offset: '40%' });
	        } else {
	        	$('footer .container').removeClass('text').addClass('show');
	        }
	        

	        $('.container').waypoint(function(direction){
	        	if ('down' === direction){
	        		$('.article').removeClass('text').addClass('show');
	        	}
	        }, { offset: '90%' });

	        $('.container').waypoint(function(direction){
	        	if ('down' === direction){
	        		$('.article--single').removeClass('text').addClass('show');
	        	}
	        }, { offset: '90%' });


	        $('.container').waypoint(function(direction){
	        	if ('down' === direction){
	        		$('.person').removeClass('text').addClass('show');
	        	}
	        }, { offset: '40%' });


	      

	// Initialize wheel animation
	initializeWheelAnimation();

	initializeBirthdayInput();
})

function initializeWheelAnimation() {
	var useTagWidth = $('use.icon-wrap').attr('width');
	var scale = 1.5;
	var hoverWidth = useTagWidth * scale;

	$('a.item').mouseover(function() {
		var useTag = $(this).children('use.icon-wrap');
		useTag.data('original-x', useTag.attr('x'))
		      .data('original-y', useTag.attr('y'));
		var x = Math.round(useTag.attr('x'));
		var y = Math.round(useTag.attr('y'));
		useTag.attr('x', x - (hoverWidth - useTagWidth) / 2);
		useTag.attr('y', y - (hoverWidth - useTagWidth) / 2);
		useTag.attr('width', hoverWidth);
		useTag.attr('height', hoverWidth);
	}).mouseout(function() {
		var useTag = $(this).children('use.icon-wrap');
		useTag.attr('x', useTag.data('original-x'));
		useTag.attr('y', useTag.data('original-y'));
		useTag.attr('width', useTagWidth);
		useTag.attr('height', useTagWidth);
	});	
}
// Show "press enter" label when day/month/year have values.
function initializeBirthdayInput() {

	var inputDay = $('input#day');
	var inputMonth = $('input#month');
	var inputYear = $('input#year');
	var onBirthdayChanged = function() {

		if (inputYear.val().length >= 4) {
			if (inputDay.val() >= 1 && inputDay.val() <= 31 &&
			    inputMonth.val() >= 1 && inputMonth.val() <= 12) {
				$('#label-press-enter').css('display', 'block');
				$('#label-try-again').css('display', 'none');
			} else if (inputDay.val() < 1 || inputDay.val() > 31 &&
			    inputMonth.val() < 1 || inputMonth.val() > 12) {
				$('#label-press-enter').css('display', 'none');
				$('#label-try-again').css('display', 'block');
			}
		}
		else {
			$('#label-press-enter').css('display', 'none');

			$('#label-try-again').css('display', 'none');
		}
	}
	inputDay.on('input', onBirthdayChanged);
	inputMonth.on('input', onBirthdayChanged);
	inputYear.on('input', onBirthdayChanged);
}
