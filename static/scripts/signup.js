function togglePassword(inputId) {
    // Get the password input element by its ID
    const passwordInput = document.getElementById(inputId);

    // Get the toggle button element using a query selector
    const toggleBtn = document.querySelector(`[for=${inputId}] .toggle-password`);

    // Check the current type of the password input
    if (passwordInput.type === "password") {
        // If it's a password field, change it to a text field
        passwordInput.type = "text";
    } else {
        // If it's a text field, change it to a password field
        passwordInput.type = "password";
    }
}