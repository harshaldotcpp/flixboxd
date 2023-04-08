const watch_btn = document.querySelector("#watch-btn");
const like_btn = document.querySelector("#like_btn");
const watchlist_btn = document.querySelector("#watchlist_btn");
const review_btn = document.querySelector("#review-btn");
const review_cancel_btn = document.querySelector("#review-cancel-btn");
const stars_btns = document.getElementsByClassName("star-btn")



var date = new Date();

var day = date.getDate();
var month = date.getMonth() + 1;
var year = date.getFullYear();

if (month < 10) month = "0" + month;
if (day < 10) day = "0" + day;

var today = year + "-" + month + "-" + day;

function myAlert(message) {
    console.log("hii")
    document.querySelector("#alert-msg").innerHTML = message;
    document.querySelector("#frontend-alert").classList.remove("hidden")
    console.log(document.querySelector("#frontend-alert"))
    setTimeout(() => {
        document.querySelector("#frontend-alert").classList.add("hidden");
    }, 1299);
    return;


}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;

}
const csrftoken = getCookie('csrftoken');

const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    mode: 'same-origin',
    body: "",
}

const date_picker = document.getElementById('datePicker')
if (date_picker) {
    date_picker.value = today;
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
        Array.from(stars_btns).forEach(element => {
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
                console.log("wow")
                myAlert(response.message);
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