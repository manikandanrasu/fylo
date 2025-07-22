// Show or hide navbar on click

const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");

menuBtn.addEventListener("click", () => {
    navLinks.classList.toggle("open");
    navLinks.classList.toggle("active");
});