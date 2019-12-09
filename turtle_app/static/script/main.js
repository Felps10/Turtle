console.log("Javascript works");

// https://www.w3schools.com/howto/howto_js_typewriter.asp
let i = 0;
let txt = "Meet Turtle, your new e-market.";
let speed = 50;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("clickme-message").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
