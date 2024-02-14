function displayLoginfields (){
    let loginbox = document.querySelector(".login-box");
        loginbox.innerHTML = `<form>
    <input type="text" name="username" placeholder="Username or Email">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>`;
}

function dispaySignupfields (){
    let loginbox = document.querySelector(".login-box");
    loginbox.innerHTML = `<form>
    <input type="text" name="lawfirmName" placeholder="Lawfirm Name">
    <input type="text" name="registrationNumber" placeholder="Registration Number">
    <input type="tel" name="phoneNumber" placeholder="Phone Number">
    <input type="email" name="email" placeholder="Email Address">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Sign Up</button>
</form>`
;
}

document.addEventListener("DOMContentLoaded", function() {
    let loginButton = document.getElementById("login-button");
    let signupButton = document.getElementById("signup-button");

    loginButton.addEventListener("click", displayLoginfields);
    signupButton.addEventListener("click", dispaySignupfields);
});

