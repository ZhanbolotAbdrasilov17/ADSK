const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const carousel = document.querySelector(".carousel-container");
const track = document.querySelector(".track");
let width = carousel.offsetWidth;
let index = 0;
window.addEventListener("resize", function () {
  width = carousel.offsetWidth;
});
next.addEventListener("click", function (e) {
  e.preventDefault();
  index = index + 1;
  prev.classList.add("show");
  track.style.transform = "translateX(" + index * -width + "px)";
  if (track.offsetWidth - index * width < index * width) {
       index = 1
  }

});
prev.addEventListener("click", function () {
  index = index - 1;
  next.classList.remove("hide");
  if (index <= 0) {
    index = 3
  }
  track.style.transform = "translateX(" + index * -width + "px)";
});


//Burger menu
let menuBtn = document.querySelector('.navbar-toggler');
let menu = document.querySelector('#navbarSupportedContent');
menuBtn.addEventListener('click', function(){
	menu.classList.toggle('active');
})


var player
function onYouTubePlayerAPIReady() {
  player = new YT.Player("mainVideo", {
    events: {
      onReady: onPlayerReady
    }
  });
}

function onPlayerReady(event) {
  var playButton = document.querySelector(".slider__video");
  playButton.addEventListener("click", function () {
    player.playVideo();
  });
}

// Inject YouTube API script
var tag = document.createElement("script");
tag.src = "//www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
