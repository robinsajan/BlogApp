let nav = document.getElementById("nav");
let title = document.getElementById("title-tag");
let demi_title = document.getElementById("demi-title-tag");
let fixed_social_link = document.querySelector(".fixed-social-links");
let footer = document.getElementById("footer");

window.addEventListener("scroll", () => {
  var footerDistance = window.pageYOffset + footer.getBoundingClientRect().top;
  if (window.pageYOffset > 80) {
    title.innerHTML = demi_title.innerText;
    nav.childNodes[1].innerText == "Robin";
    nav.classList.add("nav-js-style");
    fixed_social_link.classList.add("fixed-social-links-js-style");
  } else {
    title.innerHTML = "Blog App";
    nav.classList.remove("nav-js-style");
    fixed_social_link.classList.remove("fixed-social-links-js-style");
  }
  if (window.pageYOffset > footerDistance - 500) {
    fixed_social_link.classList.remove("fixed-social-links-js-style");
  }
});

let search_btn = document.getElementById("search-btn");
let search_page = document.querySelector(".search-page");
let close_btn = document.getElementById("close-btn");
let navbar = document.querySelector(".nav-bar");
let body = document.getElementById("body");

search_btn.addEventListener("click", () => {
  navbar.classList.remove("nav-bar-js");
  search_page.classList.toggle("search-page-js");
  body.style.overflowY = "hidden";
});
close_btn.addEventListener("click", () => {
  search_page.classList.toggle("search-page-js");
  body.style.overflowY = "visible";
});

let burger = document.getElementById("burger");

burger.addEventListener("click", () => {
  console.log("Hello")
  
  navbar.classList.toggle("nav-bar-js");
});
