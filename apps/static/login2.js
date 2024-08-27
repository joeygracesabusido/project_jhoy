document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");

    const login = async () => {
        var username = document.querySelector('#username').value;
        var password = document.querySelector('#password').value;

        const search_url = `/api-login/?username1=${username}&password1=${password}`;

        try {
            const response = await fetch(search_url);
            const data = await response.json();

            console.log(data);

            if (response.ok) {
                window.location.assign("/dashboard/");
                // if (data === null) {
                //     document.querySelector('#alert').innerHTML = 'User is not registered';
                // } else {
                //     // Login successful
                //     console.log("Login successful");
                //     window.location.assign("/dashboard/");
                // }
            } else if (response.status === 400) {
                // Incorrect password or username
                document.querySelector('#alert').innerHTML = 'Password & Username did Not Match';
            }else if (response.status === 401) {
                // Incorrect password or username
                document.querySelector('#alert').innerHTML = 'Username is Not Register';
            }
            
            else if (response.status === 500) {
                // Server error
                document.querySelector('#alert').innerHTML = 'Server Error';
            } else {
                // Other errors
                document.querySelector('#alert').innerHTML = 'Error: ' + response.statusText;
            }
        } catch (error) {
            // Network or fetch error
            console.error('Error:', error);
            document.querySelector('#alert').innerHTML = 'Network or Fetch Error';
        }
    };

    var loginCredential = document.querySelector('#BtnLogin');
    loginCredential.addEventListener("click", function () {
        console.log("Login button clicked");
        login();
    });

    document.querySelector('#password').addEventListener("keydown", function(event) {
        console.log("Key pressed: " + event.key);
        if (event.key === "Enter") {
            console.log("Enter key pressed");
            login();
        }
    });
});
