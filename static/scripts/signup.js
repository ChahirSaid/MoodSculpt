function togglePassword (inputId) {
  // Get the password input element by its ID
  const passwordInput = document.getElementById(inputId);

  // Get the toggle button element using a query selector
  const toggleBtn = document.querySelector(`[for=${inputId}] .toggle-password`);

  // Check the current type of the password input
  if (passwordInput.type === 'password') {
    // If it's a password field, change it to a text field
    passwordInput.type = 'text';
  } else {
    // If it's a text field, change it to a password field
    passwordInput.type = 'password';
  }
}

document.addEventListener('DOMContentLoaded', function () {
  const passwordInput = document.getElementById('password');
  const passwordStrength = document.getElementById('password-strength');
  const signUpForm = document.querySelector('form[name="signup-form"]');

  passwordInput.addEventListener('input', function () {
    const password = passwordInput.value;
    const strength = checkPasswordStrength(password);
    updatePasswordStrengthMessage(strength);

    if (strength === 'Weak') {
      signUpForm.querySelector('input[type="submit"]').disabled = true;
    } else {
      signUpForm.querySelector('input[type="submit"]').disabled = false;
    }
  });

  function checkPasswordStrength (password) {
    if (password.length < 8) {
      return 'Weak';
    } else {
      return 'Strong';
    }
  }

  function updatePasswordStrengthMessage (strength) {
    passwordStrength.textContent = 'Password Strength: ' + strength;
  }
});
