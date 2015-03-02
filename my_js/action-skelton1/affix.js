$(function(){
	$('my_affix').affix({
		offset: {
			top: 200,
			bottom: function(){
				return (this.bottom = $('.footer').outerHeight(true))
			}
		}
	});
});
