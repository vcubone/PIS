$(document).ready(function() {
    $('.one-post').hover(
        function() {
            $(this).find('.one-post-shadow').animate({opacity: 0.1}, 300);
        },
        function() {
            $(this).find('.one-post-shadow').animate({opacity: 0}, 300);
        }
    );

    $('.header img').hover(
        function() {
            $(this).animate({width: '338px'}, 200);
        },
        function() {
            $(this).animate({width: '318px'}, 200);
        }
    );
});