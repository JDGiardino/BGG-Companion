(async () => {
    function clear_table(){
        const table = document.getElementById('table');
        table.innerText = "";
    }

    async function create_table(games){
        const table = document.getElementById('table')
        const header = table.createTHead();
        const row = header.insertRow();
        row.insertCell().innerText = "Game Name (released year)"
        row.insertCell().innerText = "Overall Rank"
        row.insertCell().innerText = "Average Rating"
        row.insertCell().innerText = "Complexity"
        row.insertCell().innerText = "Players"
        games.forEach(addGamesToTable)

        function addGamesToTable(game, index){
            const row = table.insertRow();
            row.insertCell().innerText = `${game.name} (${game.yearpublished})`
            row.insertCell().innerText = `${game.overallrank}`
            row.insertCell().innerText = `${game.averagerating}`
            row.insertCell().innerText = `${game.complexity}`
            row.insertCell().innerText = `${game.minplayers} - ${game.maxplayers} players`
        }
    }

    async function get_game_collection(order_by) {
        clear_table();
        const user = document.getElementById("user").value;
        const response = await fetch(`/ordered_games?user=${user}&orderby=${order_by}`)
        if (response.ok) {
            const games = await response.json();
            await create_table(games);
        } else {
            const error_field = document.getElementById("game-error");
            error_field.innerText = await response.text();
        }
    }
    async function last_username(){
        const response = await fetch ('last_username')
        if (response.ok) {
            document.getElementById("user").value = await response.text();
        } else {
            const error_field = document.getElementById("user");
            error_field.innerText = await response.text();
        }
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
