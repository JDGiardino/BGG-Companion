function get_random_game() {
    const user = document.getElementById("user").value;
    fetch('/random_game?user='+ user)
    .then(response => response.json())
    .then(game => {
        const game_field = document.getElementById("game-name");
        game_field.innerText = game.name;
    });
}

const submit_button = document.getElementById("submit");
submit_button.addEventListener("click", get_random_game);
