(async () => {
  function clearRandomGameResponseElements() {
    document.getElementById("game-name").innerText = "";
    document.getElementById("game-thumbnail").src = "";
    document.getElementById("game-error").innerText = "";
  }

  async function getRandomGame() {
    clearRandomGameResponseElements();
    const user = document.getElementById("user").value;
    const minplayers = document.getElementById("number-of-players-min").value;
    const maxplayers = document.getElementById("number-of-players-max").value;
    let playerrangetype;
    if (document.getElementById("normal-range-players").checked) {
      playerrangetype = "normal";
    } else if (document.getElementById("exact-range-players").checked) {
      playerrangetype = "exact";
    }
    else playerrangetype = "";
    let playstyle;
    if (document.getElementById("competitive").checked){
      playstyle = "competitive";
    } else if (document.getElementById("cooperative").checked){
      playstyle = "cooperative";
    }
    else playstyle = "";

    const response = await fetch(
      `/random_game?user=${user}&minplayers=${minplayers}&maxplayers=${maxplayers}&playerrangetype=${playerrangetype}&playstyle=${playstyle}`
    );
    if (response.ok) {
      const game = await response.json();
      const game_field = document.getElementById("game-name");
      game_field.innerHTML +=
        game.name.link("https://boardgamegeek.com/boardgame/" + game.id) +
        `  (${game.yearpublished})`;

      const img = document.getElementById("game-thumbnail");
      img.src = game.image;
      img.height = "300";
      img.width = "300";
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

  async function pageVisits() {
    const response = await fetch("page_visit_counter");

    if (response.ok) {
      const page_visits = await response.text();
      const page_visits_field = document.getElementById("page-visits");
      page_visits_field.innerText = page_visits;
    } else {
      const error_field = document.getElementById("page-visits");
      error_field.innerText = await response.text();
    }
  }
  const submit_button = document.getElementById("submit");
  submit_button.addEventListener("click", () => getRandomGame());

  await lastUsername();
  await pageVisits();
})();
