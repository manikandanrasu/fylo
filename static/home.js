// Show or hide navbar on click

const user = document.getElementById("user-profile");
const userMenu = document.getElementById("user-menu");

user.addEventListener("click", () => {
    userMenu.classList.toggle("open");
});

 // menu.classList.toggle("active");