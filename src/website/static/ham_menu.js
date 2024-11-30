function menu() {
    var x = document.getElementById("nav_links");
    console.log(x.style.display)
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }