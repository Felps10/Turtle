console.log("Javascript works");

// https://www.w3schools.com/howto/howto_js_typewriter.asp

// LANDING PAGE MESSAGE NOT LOGGED
let i = 0;
let welcomeMsg = "Meet Turtle, your new e-market.";
let speed = 50;

function sendWelcomeMsg() {
  if (i < welcomeMsg.length) {
    document.getElementById("clickme-message").innerHTML += welcomeMsg.charAt(
      i
    );
    i++;
    setTimeout(sendWelcomeMsg, speed);
  }
}

// LANDING PAGE LOGGED
let loggedMsg =
  "Hey, don't worry! Remember that Turtle will always be by your side.";

function sendLoggedMsg() {
  if (i < loggedMsg.length) {
    document.getElementById("logged-message").innerHTML += loggedMsg.charAt(i);
    i++;
    setTimeout(sendLoggedMsg, speed);
  }
}
