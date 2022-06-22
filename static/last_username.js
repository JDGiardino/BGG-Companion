fetch('last_username')
    .then(async response => {
        if (response.ok) {
            const user = await response.text();
            document.getElementById("user").value = user;
        } else {
            const error_field = document.getElementById("user");
            error_field.innerText = await response.text();
        }
    });