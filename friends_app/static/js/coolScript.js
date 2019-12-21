$(document).ready(function() {
    $(".details-content").each(function() {
        $(this).css("height", $(this).height()+"px");
        $(this).hide();
    })
    $('.hidden').animate({'opacity': 1}, 3000);
});

getNewEpisode = () => {
    window.location.reload()
}

showOrHideDetails = () => {
    var details = $(".details-content");
    details.slideToggle(400);
    details.css("display", "flex");
    $("#friends-logo-image").css("width", "500px");
}