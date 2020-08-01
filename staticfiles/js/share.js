const share = document.querySelector(".slideshow");
const shareBtn = document.querySelector("#shareBtn");

const OPEN_CLASS = "slideshow_open";

function shareClick() {
  const currentClass = share.className;
  if (currentClass !== OPEN_CLASS) {
    share.className = OPEN_CLASS;
  } else {
    share.className = "slideshow";
  }
}

function init() {
  shareBtn.addEventListener("click", shareClick);
}

init();
