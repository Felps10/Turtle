console.log("Javascript works");

// https://www.w3schools.com/howto/howto_js_typewriter.asp

// LANDING PAGE MESSAGE NOT LOGGED
let i = 0;
let notLoggedMessage = "Meet Turtle, your new e-market.";
let speed = 50;

function sendNLMessage() {
  if (i < notLoggedMessage.length) {
    document.getElementById(
      "clickme-message"
    ).innerHTML += notLoggedMessage.charAt(i);
    i++;
    setTimeout(sendNLMessage, speed);
  }
}

// LANDING PAGE LOGGED
let;
