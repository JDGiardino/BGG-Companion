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
    row.insertCell().innerText = "Complexity";
    row.insertCell().innerText = "Players";
    games.forEach(addGamesToTable);

    function addGamesToTable(game) {
      const row = table.insertRow();
      row.insertCell().innerText = `${game.name} (${game.yearpublished})`;
      row.insertCell().innerText = `${game.overallrank}`;
      row.insertCell().innerText = `${game.complexity}`;
      row.insertCell().innerText = `${game.minplayers} - ${game.maxplayers} players`;
    }
  }

  function getGameCollectionParameters() {
    const user = document.getElementById("user").value;
    const playstyle = document.getElementById("playstyle").value;
    let gametype = document.getElementById("gametype").value;
    if (gametype == "Board Games") {
      gametype = "boardgame";
    }
    if (gametype == "Board Game Expansions") {
      gametype = "boardgameexpansion";
    }

    return {
      user: user,
      playstyle: playstyle,
      gametype: gametype,
    };
  }

  async function getGameCollectionTable(order_by) {
    clearTable();
    let parameters = getGameCollectionParameters();
    const response = await fetch(
      `/ordered_games?user=${parameters.user}&orderby=${order_by}&playstyle=${parameters.playstyle}` +
        `&gametype=${parameters.gametype}`
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
  const complexity_button = document.getElementById("complexity");
  alphabetical_button.addEventListener("click", () =>
    getGameCollectionTable("alphabet")
  );
  overall_rank_button.addEventListener("click", () =>
    getGameCollectionTable("rank")
  );
  complexity_button.addEventListener("click", () =>
    getGameCollectionTable("complexity")
  );

  /*eslint-disable */
  const table2excel = new Table2Excel();
  /*eslint-enable */
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
