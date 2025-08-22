// Get references to the HTML elements we need to interact with
const heading = document.getElementById('main-heading');
const button = document.getElementById('change-text-btn');

// Define a function that will be executed when the button is clicked
function changeText() {
    heading.textContent = "Button Clicked!";
}

// Add an event listener to the button
// When the 'click' event occurs, call the 'changeText' function
button.addEventListener('click', changeText);