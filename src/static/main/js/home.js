
console.log("hii")


$("#direct-log-btn").click((event) => {
    document.querySelector("#log-movie-search").focus();
    console.log(document.querySelector("#log-movie-search"))
    $("#log-search-field-top").toggleClass("hidden");

});


$("#log-movie-search").on("input", (event) => {
    const input_value = event.target.value;
    let url = "https://api.themoviedb.org/3/search/movie?api_key=88e01c9c6c65ce312ee50a4358e089ac&query=" + input_value;

    fetch(url)
        .then((response) => response.json())
        .then(response => {
            document.getElementById("log-result_list").innerHTML = "";
            movies = []
            if (response.total_results == 0)
                return;

            for (let i = 0; i < 8; i++) {
                if (response.results[i]) {
                    movies.push({
                        name: response.results[i].title,
                        release_date: response.results[i].release_date.slice(0, 4),
                        poster_path: response.results[i].poster_path,
                        id: response.results[i].id,
                    });
                }
            }

            movies.forEach(movie => {
                $("#log-result_list").append(`<li class="lsri hover:bg-letterboxd-4 py-2 px-2" onclick=handleLogSelection(event) data-name="${movie.name}" data-release_year="${movie.release_date}" data-poster_path="${movie.poster_path}" data-id="${movie.id}" >${movie.name} (${movie.release_date})</li>`);
            });
        });
});


$("#log-search-cancel").click(event => {
    document.getElementById("log-result_list").innerHTML = "";
    $("#log-search-field-top").toggleClass("hidden");
});



function setInputValue(dataset) {
    $('#ready-log-tmdb-id').val(dataset.id);
    $('#ready-log-name').val(dataset.name);
    $('#ready-log-poster-path').val(dataset.poster_path);
    $('#ready-log-release-year').val(dataset.release_year);
}

function handleLogSelection(event) {
    document.getElementById("log-result_list").innerHTML = "";
    fetch(`/film/isliked/${event.target.dataset.id}`, options)
        .then(response => response.json()).then(response => {
            if (response.isliked){
                $("#direct-log-like-icon").addClass("fill-letterboxd-5");
                $("#direct-log-like").prop("checked",true);
                return;
            }
            $("#direct-log-like-icon").removeClass("fill-letterboxd-5");
            $("#direct-log-like").prop("checked",false);
        })

    fetch(`/film/getstars/${event.target.dataset.id}`, options).
    then(response =>  response.json() ).then(response=>{
        let stars = "." + (response.stars + "").replace(".","-") ;
        console.log(stars);
        $(stars).prop("checked",true); 
    })
    $("#log-search-field-top").toggleClass("hidden");
    $("#globle-movie-review-log").toggleClass("hidden");



    const img_url = "https://image.tmdb.org/t/p/original" + event.target.dataset.poster_path;
    $("#globle-film-log-img").attr("src", img_url);
    $("#globle-log-movie-name").append(`${event.target.dataset.name} (${event.target.dataset.release_year})`);
    setInputValue(event.target.dataset);
};

$("#direct-log-review-cancel-btn").click((event) => {
    $("#globle-movie-review-log").toggleClass("hidden");
    console.log("hidden");
    $("#globle-log-movie-name").empty();
    $("#ready-log-rating").val("ignore");
    cleanUpStars()
});

$("#direct-log-like").click(event => {
    $("#direct-log-like-icon").toggleClass("fill-letterboxd-5")
});


$(".star-btn").each(function(){
    let btn = this;
    $(btn).click((event)=>{
        $("#ready-log-rating").val("ignore");
    });
});


function cleanUpStars(){
    $(".star-btn").each((i,stars)=>{
        $(stars).prop("checked",false);
    });
}


$("#clear-stars").click(event=>{
    event.preventDefault()
    $("#ready-log-rating").val("remove");
    cleanUpStars();
});




var today = getTodaysDate();

const log_date_picker = document.getElementById('log-datePicker')
if (log_date_picker) {
    log_date_picker.value = today;
    log_date_picker.ariaPlaceholder = today;
}