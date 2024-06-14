function openPopup() {
  document.getElementById("login").style.display = "flex";
}

function closePopup() {
  document.getElementById("login").style.display = "none";
}

function openNestedPopup() {
  window.location.hash = 'register';
  document.getElementById("registered").style.display = "flex";
  document.getElementById("login").style.display = "none";
}

function closeNestedPopup() {
  document.getElementById("registered").style.display = "none";
}
