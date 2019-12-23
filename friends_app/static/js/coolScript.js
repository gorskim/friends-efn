var switchText;

animateOpacity = (selector, value, time) => {
    $(selector).animate({'opacity': value}, time);
}

getNewEpisode = () => {
    window.location.reload()
};

$(document).ready(function() {
    animateOpacity('.hidden', 1, 3000);
    animateOpacity('.btn-switch', 1, 3000);
    switchText = document.getElementsByClassName("btn-switch")[0].innerHTML;
});

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
};