// Show or hide navbar on click

const user = document.getElementById("user-profile");
const userMenu = document.getElementById("user-menu");

user.addEventListener("click", () => {
    userMenu.classList.toggle("open");
});

// send user input to backend 

const generateBtn = document.getElementById("generateBtn");
const userInput = document.getElementById("userInput");
const output = document.getElementById("output");

// Function to show alert if input box empty

function showAlert(message){
    const alertBox = document.getElementById("alertMsg");
    alertBox.innerText = message;
    alertBox.classList.add("show")

    setTimeout(() => {
        alertBox.classList.remove("show")
    }, 3000);

}

async function sendText() {
    const text = userInput.value.trim();

    if (text === ""){
        return showAlert("please write something")
    }
    try {
        const res = await fetch("api/generate", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrf_token,
                "Content-Type":"application/json"
            },
            body: JSON.stringify({ text })
        });
    }
    catch (err) {

    }
}

generateBtn.addEventListener("click", sendText);