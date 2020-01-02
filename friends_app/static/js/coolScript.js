var switchText;

$(document).ready(function() {
    idleTime();
    $('.hidden').animate({'opacity': 1}, 3000);
    $('.btn-switch').animate({'opacity': 1}, 3000);
    switchText = document.getElementsByClassName("btn-switch")[0].innerHTML
});

animateOpacity = (selector, value, time) => {
    $(selector).animate({'opacity': value}, time);
}

getNewEpisode = () => {
    window.location.reload()
};

changeDisplay = () => {
    if ($('.hidden').css("opacity") == 1) {
        showDetails();
    }
    else if ($('.details').css("opacity") == 1) {
        showMessage();
    }
};

showDetails = () => {
    animateOpacity('.hidden', 0, 1000);
    animateOpacity('.details', 1, 1000);
    switchText = "Take me back!";
};

showMessage = () => {
    animateOpacity('.details', 0, 1000);
    animateOpacity('.hidden', 1, 1000);
    switchText = "Tell me more!";
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
        time = setTimeout(pulsateLogo, 30000)
    }
}
