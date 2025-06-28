// Function to set a cookie
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// Function to get a cookie value
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Function to delete a cookie
function eraseCookie(name) {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}

// Example usage:
// Assume user has logged in successfully and you have obtained an authentication token or session ID

// Store the authentication token in a cookie
var authToken = "exampleAuthToken123";
setCookie("authToken", authToken, 7); // Cookie expires in 7 days

// To retrieve the authentication token later (for subsequent requests):
var storedAuthToken = getCookie("authToken");
if (storedAuthToken) {
    // Token found, proceed with making authenticated requests
    console.log("Authenticated request with token:", storedAuthToken);
} else {
    // Token not found, user may not be authenticated
    console.log("No authentication token found.");
}

// To logout and remove the authentication token:
eraseCookie("authToken");
console.log("Logged out. Authentication token deleted.");
