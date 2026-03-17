$(document).ready(function() {
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.header img');

    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();

        $parallaxElements.each(function(index) {
            var speed = 0.15 * (index + 1);
            var yPos = scrolled * speed;
            $(this).css({top: yPos});
        });

        $logo.css({
            transform: 'translateY(' + scrolled * 0.5 + 'px)'
        });
    });
});