function opendes() {
  document.getElementById("details").style.display = "block";
  document.getElementById("addd").style.display = "none";
  document.getElementById("rew").style.display = "none";
  document.getElementById("rev1").style.border= "none";
  document.getElementById("rev1").style.color= "black";
  document.getElementById("rev1").style.fontWeight= "normal";
  document.getElementById("add1").style.border= "none";
  document.getElementById("add1").style.color= "black";
  document.getElementById("add1").style.fontWeight= "normal";
  document.getElementById("desc1").style.border= "3px solid #1C4E8E";
  document.getElementById("desc1").style.color= "#1C4E8E";
  document.getElementById("desc1").style.fontWeight="bold" ;
  document.getElementById("desc1").style.borderRight="none" ;
  document.getElementById("desc1").style.borderLeft= "none";
  document.getElementById("desc1").style.borderTop= "none";
  document.getElementById("desc1").style.paddingTop= "none";
}
function openadd() {
  document.getElementById("addd").style.display = "block";
  document.getElementById("details").style.display = "none";
  document.getElementById("rew").style.display = "none";
  document.getElementById("rev1").style.border= "none";
  document.getElementById("rev1").style.color= "black";
  document.getElementById("rev1").style.fontWeight= "normal";
  document.getElementById("desc1").style.border= "none";
  document.getElementById("desc1").style.color= "black";
  document.getElementById("desc1").style.fontWeight= "normal";
  document.getElementById("add1").style.border= "3px solid #1C4E8E";
  document.getElementById("add1").style.color= "#1C4E8E";
  document.getElementById("add1").style.fontWeight="bold" ;
  document.getElementById("add1").style.borderRight="none" ;
  document.getElementById("add1").style.borderLeft= "none";
  document.getElementById("add1").style.borderTop= "none";
  document.getElementById("add1").style.paddingTop= "none";
}
function openrev() {
  document.getElementById("details").style.display = "none";
  document.getElementById("addd").style.display = "none";
  document.getElementById("rew").style.display = "block";
  document.getElementById("desc1").style.border= "none";
  document.getElementById("desc1").style.color= "black";
  document.getElementById("desc1").style.fontWeight= "normal";
  document.getElementById("add1").style.border= "none";
  document.getElementById("add1").style.color= "black";
  document.getElementById("add1").style.fontWeight= "normal";
  document.getElementById("rev1").style.border= "3px solid #1C4E8E";
  document.getElementById("rev1").style.color= "#1C4E8E";
  document.getElementById("rev1").style.fontWeight="bold" ;
  document.getElementById("rev1").style.borderRight="none" ;
  document.getElementById("rev1").style.borderLeft= "none";
  document.getElementById("rev1").style.borderTop= "none";
  document.getElementById("rev1").style.paddingTop= "none";
}
function changep(){
  console.log("entered");
 document.getElementById("pricee").innerHTML="$1750.00";
}
function addtocart(){
  window.location.hash = 'cart';
  console.log(document.getElementById("cart-countt").innerHTML)
  let strToNum = parseInt(document.getElementById("cart-countt").innerHTML, 10);
  strToNum+=parseInt(document.getElementById("quanity").value,10)
  console.log(strToNum)
  document.getElementById("cart-countt").innerHTML=strToNum;
}
function minicart(){
  console.log("entered");
 document.getElementById("mini").style.display="block";
}
function deletecart(){
  var el = document.getElementById('delete');
var closestParent = el.parentNode.closest('div');
console.log(closestParent);
}



