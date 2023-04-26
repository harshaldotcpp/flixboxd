const watch_btn = document.querySelector("#watch-btn");
const like_btn = document.querySelector("#like_btn");
const watchlist_btn = document.querySelector("#watchlist_btn");
const review_btn = document.querySelector("#review-btn");
const review_cancel_btn = document.querySelector("#review-cancel-btn");



var today = getTodaysDate();

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

        let iswatched = false;
        if (watch_btn.dataset.iswatched === "true") {
            iswatched = false;
            watch_btn.dataset.iswatched = "false";
        } else {
            iswatched = true;
            watch_btn.dataset.iswatched = "true";
        }



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
            add: iswatched,
            tmdb_id: getCookie('id'),

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
        let islike = false;
        if (like_btn.dataset.islike === "true") {
            islike = false;
            like_btn.dataset.islike = false;
        } else {
            islike = true;
            like_btn.dataset.islike = true;
        }

        options.body = JSON.stringify({
            add: islike,
            tmdb_id: getCookie('id'),
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

        let iswatchlist;
        if (watchlist_btn.dataset.iswatchlist === "true") {
            iswatchlist = false;
            watchlist_btn.dataset.iswatchlist = "false";
        } else {
            iswatchlist = true;
            watchlist_btn.dataset.iswatchlist = "true";
        }
        options.body = JSON.stringify({
            add: iswatchlist,
            tmdb_id: getCookie('id'),
        });


        fetch("/film/watchlistadd", options)
            .then(response => response.json())
            .then((response) => {
                myAlert(response.message);
            })

    });


}


const add_movie_into_list = document.getElementsByClassName("add-movie-into-list");

Array.from(add_movie_into_list).forEach(btn => {
    btn.addEventListener('click', (event) => {
        console.log(btn.dataset.movie_id);
        console.log(btn.dataset.list_id);
        options.body = JSON.stringify({
            movie_id: btn.dataset.movie_id,
            list_id: btn.dataset.list_id,
        });
        console.log(options)

        fetch("/lists/addmovie", options).then(response => response.json())
            .then((response) => {
                myAlert(response.message);
            });
        const movie_add = document.getElementById("add-to-list");
        movie_add.classList.add("hidden")
    });
});

document.getElementById("add-to-list-btn").addEventListener("click", (event) => {
    const movie_add = document.getElementById("add-to-list");
    movie_add.classList.toggle("hidden")
});

like_review_btns = document.getElementsByClassName("like-review-btn")

Array.from(like_review_btns).forEach(like_review_btn=>{
    like_review_btn.addEventListener("click",(event)=>{
        const review_id = like_review_btn.dataset.review_id
        const username = like_review_btn.dataset.username
        const value = like_review_btn.checked 
        console.log(review_id)
        console.log(username)

        const review_icon = document.querySelector(`.review-icon-${like_review_btn.id}`);
        review_icon.classList.toggle("fill-letterboxd-5")

        options.body = JSON.stringify({
            review_id:review_id,
            username:username,
            addlike:value,
        });

        fetch("/reviews/like",options);
    });
});