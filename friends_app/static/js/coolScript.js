$(document).ready(function() {
    idleTime();
    $('.hidden').animate({'opacity': 1}, 3000);
    $('.btn-switch').animate({'opacity': 1}, 3000);
});

getNewEpisode = () => {
    window.location.reload();
}

changeDisplay = () => {
    if ($('.hidden').css("opacity") == 1) {
        showDetails();
    }
    else if ($('.details').css("opacity") == 1) {
        showMessage();
    }
}

showDetails = () => {
    $('.hidden').animate({'opacity': 0}, 1000);
    $(".details").animate({'opacity': 1}, 1000);
    document.getElementsByClassName("btn-switch")[0].innerHTML = "Take me back!";
}

showMessage = () => {
    $(".details").animate({'opacity': 0}, 1000);
    $('.hidden').animate({'opacity': 1}, 1000);
    document.getElementsByClassName("btn-switch")[0].innerHTML = "Tell me more!";
}

var idleTime = function() {
    var time;
    window.onload = resetIdleTime;
    document.onmousemove = resetIdleTime;
    document.onkeypress = resetIdleTime;

    function pulsateLogo() {
        $('#friends-logo-image').addClass('pulse')
        }

    function resetIdleTime() {
        clearTimeout(time);
        $('#friends-logo-image').removeClass('pulse')
        console.log('reset')
        time = setTimeout(pulsateLogo, 30000)
    }
}