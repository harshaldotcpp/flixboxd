var dragSrcEl = null;
console.log("hello")

function updateTopFour() {

    const cards = document.querySelectorAll(".grid-container .grid-item");

    let top4 = [];
    Array.from(cards).forEach((card, i) => {
        if (card.dataset.isnone == "false")
            top4.push({
                is_present: true,
                id: card.dataset.id,
                poster_path: card.dataset.poster_path
            })
        else
            top4.push({
                is_present: false,
                id: "none",
                poster_path: "none"
            })

    });

    options.body = JSON.stringify(top4);
    myAlert("top list updated");
    const username = getCookie("username");
    fetch(`/${username}/updatetop`, options);
}


function handleDragStart(e) {
    this.style.opacity = "0.4";
    dragSrcEl = this;
    e.dataTransfer.effectAllowed = "move";
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault();
    }
    e.dataTransfer.dropEffect = "move";
    return false;
}

function handleDragEnter(e) {
    this.classList.add("over");
}

function handleDragLeave(e) {
    this.classList.remove("over");
}

function handleDrop(e) {
    if (e.stopPropagation) {
        e.stopPropagation();
    }

    if (dragSrcEl != this) {
        this.replaceWith(this, dragSrcEl);
    }
    updateTopFour()
    return false;
}

function handleDragEnd(e) {
    this.style.opacity = "1";
    items.forEach(function (item) {
        item.classList.remove("over");
    });
}
let items = document.querySelectorAll(".grid-container .grid-item");
items.forEach(function (item) {
    item.addEventListener("dragstart", handleDragStart, false);
    item.addEventListener("dragenter", handleDragEnter, false);
    item.addEventListener("dragover", handleDragOver, false);
    item.addEventListener("dragleave", handleDragLeave, false);
    item.addEventListener("drop", handleDrop, false);
    item.addEventListener("dragend", handleDragEnd, false);
});



const top_remove_btn = document.getElementsByClassName("top-remove-btn");
Array.from(top_remove_btn).forEach((btn) => {
    btn.addEventListener("click", (event) => {
        console.log('remove card no ' + btn.dataset.cardno)
        const node = document.getElementById(btn.dataset.cardno);
        node.setAttribute("data-isnone", "true")
        const addbtn = document.getElementById("add" + btn.dataset.cardno)
        addbtn.classList.remove("hidden");
        btn.classList.add("hidden");
        updateTopFour();

    })
})



let position_to_be_inserted;
let addButtons = document.querySelectorAll(".top4add");
const search_input = document.getElementById("movie-search")

Array.from(addButtons).forEach(btn => {
    btn.addEventListener("click", event => {
        document.getElementById("search-field-top").classList.toggle("hidden")
        position_to_be_inserted = btn.dataset.position;
        search_input.focus()
    })
})


function movieSelected(event) {
    const id = event.target.dataset.id;
    let poster_path = "https://image.tmdb.org/t/p/original" + event.target.dataset.poster_path;
    const main_card = document.getElementById(position_to_be_inserted);
    const image = document.getElementById("img" + position_to_be_inserted);
    const addBtn = document.getElementById("add" + position_to_be_inserted);

    main_card.setAttribute("data-id", id);
    main_card.setAttribute("data-poster_path", event.target.dataset.poster_path);
    main_card.setAttribute("data-isnone", "false");

    poster_path = "https://image.tmdb.org/t/p/w200" + event.target.dataset.poster_path;
    image.setAttribute("src", poster_path);
    addBtn.classList.add("hidden");
    document.getElementById("search-field-top").classList.toggle("hidden")
    document.getElementById("top-remove-btn-" + position_to_be_inserted).classList.remove("hidden");

    updateTopFour();
}
search_input.addEventListener("input", (event) => {
    const input_value = search_input.value.replaceAll(" ", "%20");
    let url = "https://api.themoviedb.org/3/search/movie?api_key=88e01c9c6c65ce312ee50a4358e089ac&query=" + input_value;

    fetch(url).then(response => response.json())
        .then(response => {
            document.getElementById("result_list").innerHTML = "";
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
                const classes = ["hover:bg-letterboxd-4", "py-2", "px-2"];
                const li = document.createElement('li');

                li.setAttribute("data-id", movie.id);
                li.setAttribute("data-poster_path", movie.poster_path);
                li.addEventListener('click', movieSelected);
                classes.forEach(c => {
                    li.classList.add(c);
                })
                const li_content = document.createTextNode(`${movie.name} (${movie.release_date})`);
                li.appendChild(li_content);

                const ul = document.getElementById("result_list");
                ul.append(li);

            })
        });
});