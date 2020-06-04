$(".btn").click(function () {
    $("#menu,.page_cover,html").addClass("open");
    window.location.hash = "#menu";
});

window.onhashchange = function () {
    if (location.hash != "#menu") {
        $("#menu,.page_cover,html").removeClass("open");
    }
};