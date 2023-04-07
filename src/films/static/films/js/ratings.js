const rating_remove = document.getElementById("clear-rating")

Array.from(stars_btns).forEach(btn => {
    btn.addEventListener("click", event => {
        options.body = JSON.stringify({
            "rating": btn.value,
            "tmdb_id": getCookie("id"),
            "title": getCookie("movie_name"),
            "poster_path": getCookie("poster_path"),
            "director": getCookie("director")
        })
        fetch("/film/ratingadd", options).then(response => response.json())
        .then(response => {
            myAlert(response.message);
        });


        if (!watch_btn.checked) {
            watch_btn.checked = true;
            const icon = document.querySelector("#watch-icon");
            icon.classList.toggle("classList");
        }
    })
})

if (rating_remove) {
    rating_remove.addEventListener("click", event => {
        options.body = JSON.stringify({
            tmdb_id: getCookie("id"),
        });

        Array.from(stars_btns).forEach(element => {
            element.checked = false
            console.log(element)
        })
        fetch("/film/ratingremove", options)
        .then(response => response.json())
        .then(response=>{
            myAlert(response.message)
        }) 

    })
}