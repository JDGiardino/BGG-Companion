fetch('page_visit_counter')
    .then(async response => {
        if (response.ok) {
            const page_visits = await response.text();
            const page_visits_field = document.getElementById("page-visits");
            page_visits_field.innerHTML += page_visits;
        } else {
            const error_field = document.getElementById("page-visits");
            error_field.innerText = await response.text();
        }
    });