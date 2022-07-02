(async () => {
async function create_all_games_table() {
    const user = document.getElementById("user").value;
    fetch('/all_games?user=' + user)
        .then(async response => {
            if (response.ok) {
                const games = await response.json();

                const table_element = document.getElementById("table");
                let table = '';

                for(let i=0; i < games.length; i++) {
                    table += '<tr>'
                    table += '<td>' + `${games[i].name} (${games[i].yearpublished})` + '</td>';
                    table += '<td>' + `${games[i].minplayers} - ${games[i].maxplayers} players` + '</td>';
                    table += '</tr>'
                }

                table_element.innerHTML += table
            } else {
                const error_field = document.getElementById("game-error");
                error_field.innerText = await response.text();
            }
        });
}
async function last_username(){
      fetch('last_username')
            .then(async response => {
                if (response.ok) {
                    document.getElementById("user").value = await response.text();
                } else {
                    const error_field = document.getElementById("user");
                    error_field.innerText = await response.text();
                }
            });
}

const submit_button = document.getElementById("submit");
submit_button.addEventListener("click",  () => create_all_games_table());

await last_username();
})();
