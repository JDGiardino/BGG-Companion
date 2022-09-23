(async () => {
  function clearTable() {
    const table = document.getElementById("table");
    table.innerText = "";
  }

  function createTable(games) {
    const table = document.getElementById("table");
    const header = table.createTHead();
    const row = header.insertRow();
    row.insertCell().innerText = "Game Name (released year)";
    row.insertCell().innerText = "Overall Rank";
    row.insertCell().innerText = "Average Rating";
    row.insertCell().innerText = "Complexity";
    row.insertCell().innerText = "Players";
    games.forEach(addGamesToTable);

    function addGamesToTable(game) {
      const row = table.insertRow();
      row.insertCell().innerText = `${game.name} (${game.yearpublished})`;
      row.insertCell().innerText = `${game.overallrank}`;
      row.insertCell().innerText = `${game.averagerating}`;
      row.insertCell().innerText = `${game.complexity}`;
      row.insertCell().innerText = `${game.minplayers} - ${game.maxplayers} players`;
    }
  }

  async function getGameCollectionTable(order_by) {
    clearTable();
    const user = document.getElementById("user").value;
    const response = await fetch(
      `/ordered_games?user=${user}&orderby=${order_by}`
    );
    if (response.ok) {
      const games = await response.json();
      await createTable(games);
    } else {
      const error_field = document.getElementById("game-error");
      error_field.innerText = await response.text();
    }
  }
  async function lastUsername() {
    const response = await fetch("last_username");
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
  alphabetical_button.addEventListener("click", () =>
    getGameCollectionTable("alphabet")
  );
  overall_rank_button.addEventListener("click", () =>
    getGameCollectionTable("rank")
  );
  average_rating_button.addEventListener("click", () =>
    getGameCollectionTable("rating")
  );
  complexity_button.addEventListener("click", () =>
    getGameCollectionTable("complexity")
  );

  const table2excel = new Table2Excel();
  const export_collection_excel_button =
    document.getElementById("downloadexcel");
  export_collection_excel_button.addEventListener("click", function () {
    table2excel.export(
      document.querySelectorAll("#table"),
      "BoardGame Collection"
    );
  });

  await lastUsername();
})();
