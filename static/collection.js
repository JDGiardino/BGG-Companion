(async () => {
    function clear_table(){
        const table = document.getElementById('table');
        table.innerText = "";
    }

    async function create_table(games){
        const table = document.getElementById('table')
        const header = table.createTHead();
        const row = header.insertRow(0);
        const cell_one = row.insertCell(0);
        cell_one.innerText = "Game Name (released year)"
        const cell_two = row.insertCell(1);
        cell_two.innerText = "Overall Rank"
        const cell_three = row.insertCell(2);
        cell_three.innerText = "Average Rating"
        const cell_four = row.insertCell(3);
        cell_four.innerText = "Complexity"
        const cell_five = row.insertCell(4);
        cell_five.innerText = "Players"
        games.forEach(addGamesToTable)

        function addGamesToTable(game, index){
            const row = table.insertRow(index + 1);
            const cell_one = row.insertCell(0);
            cell_one.innerText = `${game.name} (${game.yearpublished})`
            const cell_two = row.insertCell(1);
            cell_two.innerText = `${game.overallrank}`
            const cell_three = row.insertCell(2);
            cell_three.innerText = `${game.averagerating}`
            const cell_four = row.insertCell(3);
            cell_four.innerText = `${game.complexity}`
            const cell_five = row.insertCell(4);
            cell_five.innerText = `${game.minplayers} - ${game.maxplayers} players`
        }
    }

    async function get_game_collection(order_by) {
        clear_table();
        const user = document.getElementById("user").value;
        fetch(`/ordered_games?user=${user}&orderby=${order_by}`)
            .then(async response => {
                if (response.ok) {
                    const games = await response.json();
                    await create_table(games);
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

    const alphabetical_button = document.getElementById("alphabetical");
    const overall_rank_button = document.getElementById("overall_rank");
    const average_rating_button = document.getElementById("average_rating");
    const complexity_button = document.getElementById("complexity");
    alphabetical_button.addEventListener("click",  () => get_game_collection("alphabet"));
    overall_rank_button.addEventListener("click",  () => get_game_collection("rank"));
    average_rating_button.addEventListener("click",  () => get_game_collection("rating"));
    complexity_button.addEventListener("click",  () => get_game_collection("complexity"));

    await last_username();
})();
