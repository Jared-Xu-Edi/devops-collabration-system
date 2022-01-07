$(function activeNav() {

    $(".active").removeClass("active");
    var current_page_URL = window.location.pathname
    $('a[href="' + current_page_URL + '"]').parent().addClass("active");

});