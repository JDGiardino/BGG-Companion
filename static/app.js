function clear_random_game_response_elements() {
    document.getElementById("game-name").innerHTML = "";
    document.getElementById("game-error").innerHTML = "";
}

async function get_random_game() {
    clear_random_game_response_elements();
    const user = document.getElementById("user").value;
    fetch('/random_game?user=' + user)
        .then(async response => {
            if (response.ok) {
                const game = await response.json();
                const game_field = document.getElementById("game-name");
                game_field.innerText = game.name;
            } else {
                const error_field = document.getElementById("game-error");
                error_field.innerText = await response.text();
            }
        });
}

const submit_button = document.getElementById("submit");
submit_button.addEventListener("click",  () => get_random_game());
