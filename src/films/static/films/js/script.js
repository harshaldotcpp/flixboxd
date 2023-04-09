const watch_btn = document.querySelector("#watch-btn");
const like_btn = document.querySelector("#like_btn");
const watchlist_btn = document.querySelector("#watchlist_btn");
const review_btn = document.querySelector("#review-btn");
const review_cancel_btn = document.querySelector("#review-cancel-btn");




var today = getTodaysDate(); 
console.log(today)

const date_picker = document.getElementById('datePicker')
if (date_picker) {
    date_picker.value = today;
    console.log(date_picker.value)
    date_picker.ariaPlaceholder = today;
}

if (review_btn) {
    review_btn.addEventListener("click", (event) => {
        document.getElementById("movie-review-log").classList.toggle("hidden");
    });
}

if (review_cancel_btn) {
    review_cancel_btn.addEventListener("click", event => {
        document.getElementById("movie-review-log").classList.toggle("hidden")
    });
}

if (watch_btn) {
    watch_btn.addEventListener("click", (event) => {


        if (!watch_btn.checked && like_btn.checked) {

            const icon = document.querySelector("#like-icon");
            icon.classList.toggle("fill-letterboxd-5")
            like_btn.checked = false;
        }


        if (watch_btn.checked && watchlist_btn.checked) {
            const icon = document.querySelector("#watchlist-icon");
            icon.classList.toggle("fill-letterboxd-4");
            watchlist_btn.checked = false;
        }
        let isRated = false;
        Array.from(document.getElementsByClassName("star-btn")).forEach(element => {
            if (element.checked === true)
                isRated = true
        })
        if (!watch_btn.checked && isRated) {
            watch_btn.checked = true;
            myAlert("there is a Activity on this film")
            return;
        }


        options.body = JSON.stringify({
            add: watch_btn.checked,
            tmdb_id: getCookie('id'),
            title: getCookie('movie_name'),
            poster_path: getCookie('poster_path'),
            director: getCookie('director'),

        });
        const icon = document.querySelector("#watch-icon");
        icon.classList.toggle("fill-letterboxd-4");

        fetch("/film/watchedadd", options)
            .then(response => {
                return response.json()
            }).then(response => {
                myAlert(response.message);
                return;
            })
    });
}

if (like_btn) {
    like_btn.addEventListener("click", (event) => {

        const icon = document.querySelector("#like-icon");
        icon.classList.toggle("fill-letterboxd-5");

        //if film liked and unwatched mark as watched liking movie also add into watched
        if (like_btn.checked && !watch_btn.checked) {

            watch_btn.checked = true;
            const icon = document.querySelector("#watch-icon");
            icon.classList.toggle("fill-letterboxd-4")

        }


        options.body = JSON.stringify({
            add: like_btn.checked,
            tmdb_id: getCookie('id'),
            title: getCookie('movie_name'),
            poster_path: getCookie('poster_path'),
            director: getCookie('director'),
        });

        fetch("/film/likedadd", options)
            .then(response => response.json())
            .then((response) => {
                myAlert(response.message);
            })

    });
}
if (watchlist_btn) {
    watchlist_btn.addEventListener("click", (event) => {

        const icon = document.querySelector("#watchlist-icon");
        icon.classList.toggle("fill-letterboxd-4");
        options.body = JSON.stringify({
            add: watchlist_btn.checked,
            tmdb_id: getCookie('id'),
            title: getCookie('movie_name'),
            poster_path: getCookie('poster_path'),
            director: getCookie('director'),
        });

        fetch("/film/watchlistadd", options)
            .then(response => response.json())
            .then((response) => {
                myAlert(response.message);
            })

    });

    document.querySelector("#maction").addEventListener("click", () => {
        document.querySelector("#movie-add").classList.toggle("hidden");
    });
}