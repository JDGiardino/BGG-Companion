(async () => {
    function clear_all_games_table(){
        const table = document.getElementById('table');
        table.innerHTML = "";
    }

async function create_all_games_table() {
    clear_all_games_table();
    const user = document.getElementById("user").value;
    fetch('/all_games?user=' + user)
        .then(async response => {
            if (response.ok) {
                const games = await response.json();
                const table = document.getElementById('table')
                games.forEach(addGamesToTable)

                function addGamesToTable(game, index){
                    const row = table.insertRow(index);
                    const cell_one = row.insertCell(0);
                    cell_one.innerHTML = `${game.name} (${game.yearpublished})`
                    const cell_two = row.insertCell(1);
                    cell_two.innerHTML = `${game.minplayers} - ${game.maxplayers} players`
                }

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
