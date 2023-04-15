const search_input = document.getElementById("movie-search")
/**
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
</svg>
**/


function saveHandle(event) {
    return "nothing for now";
}

const getAncestors = el => {
    let ancestors = [];
    while (el) {
        ancestors.unshift(el);
        el = el.parentNode;
    }
    return ancestors;
};

function handleRemove(event) {
    const list = document.getElementById("list");
    list.removeChild(event.target.parentNode.parentNode);
}

function createCancelSvg(size) {
    const path = document.createElementNS("http://www.w3.org/2000/svg", 'path');
    path.setAttribute("d", "M6 18L18 6M6 6l12 12")
    path.setAttribute("stroke-linecap", "round");
    path.setAttribute("stroke-linjoin", "round");
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("fill", "none");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("stroke-width", "i.5");
    svg.setAttribute("stroke", "currentColor");
    [`w-${size}`, `h-${size}`, "hover:stroke-letterboxd-5"].forEach(cls => {
        svg.classList.add(cls)
    });

    svg.appendChild(path);

    return svg;
}
console.log(createCancelSvg(4));

function movieSelected(event) {
    search_input.value = "";
    const data = {
        id: event.target.dataset.id,
        title: event.target.dataset.name,
        poster_path: event.target.dataset.poster_path,
        release_year: event.target.dataset.release_year,
    }

    const img = document.createElement("img");
    img.setAttribute("src", "https://image.tmdb.org/t/p/w200" + data.poster_path);
    img.setAttribute("data-src", "https://image.tmdb.org/t/p/original" + data.poster_path);
    ["lozad", "object-cover", "w-9"].forEach(cls => {
        img.classList.add(cls);
    });
    const inner_shadow = document.createElement("div");
    ["absolute", "shadow-[inset_0.1px_0.1px_3px_rgba(0,0,0,0.2)]", "shadow-white", "top-0", "left-0", "right-0", "bottom-0"].forEach(cls => {
        inner_shadow.classList.add(cls);
    });
    const card_compo = document.createElement("div");
    ["card", "relative", "rounded-sm", "self-start", "overflow-hidden"].forEach(cls => {
        card_compo.classList.add(cls);
    });
    Array.from([img, inner_shadow]).forEach(childNode => {
        card_compo.appendChild(childNode)
    });


    const movie_title = document.createElement('span');
    movie_title.appendChild(document.createTextNode(`${data.title} (${data.release_year})`));
    const add_note = document.createElement('a');
    add_note.appendChild(document.createTextNode("Add Note"));
    ["text-sm", "w-fit", "p-1", "font-myfontLight", "border", "border-letterboxd-2"].forEach(cls => {
        add_note.classList.add(cls);
    });
    const movie_info_div = document.createElement("div");
    ["flex", "flex-col", "basis-full"].forEach(cls => {
        movie_info_div.classList.add(cls);
    })

    Array.from([movie_title, add_note]).forEach(childNode => {
        movie_info_div.appendChild(childNode);
    })

    const list_item = document.createElement('div');
    ["list-element", "border", "border-letterboxd-2", "p-2", "flex", "gap-x-3", "font-abrilbold", "text-letterboxd-6", "text-lg"].forEach(cls => {
        list_item.classList.add(cls);
    });

    list_item.setAttribute("data-id", data.id);
    list_item.setAttribute("data-title", data.title);
    list_item.setAttribute("data-poster_path", data.poster_path);
    list_item.setAttribute("data-release_year", data.release_year);

    const cancel_btn = document.createElement("a");
    cancel_btn.setAttribute("id", "remove_from_list");
    ["p-2"].forEach(cls => cancel_btn.classList.add(cls))
    cancel_btn.addEventListener("click", handleRemove)

    const svg = createCancelSvg(6);
    cancel_btn.appendChild(svg);
    console.log(cancel_btn.childNodes)

    Array.from([card_compo, movie_info_div, cancel_btn]).forEach(node => {
        list_item.appendChild(node);
    });

    const list = document.getElementById("list");
    list.appendChild(list_item);
    document.getElementById("result_list").innerHTML = "";
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
                        release_year: response.results[i].release_date.slice(0, 4),
                        poster_path: response.results[i].poster_path,
                        id: response.results[i].id,
                    });
                }
            }

            movies.forEach(movie => {
                const classes = ["hover:bg-letterboxd-4", "py-2", "px-2", "searched_movie"];
                const li = document.createElement('li');

                li.setAttribute("data-id", movie.id);
                li.setAttribute("data-poster_path", movie.poster_path);
                li.setAttribute("data-name", movie.name);
                li.setAttribute("data-release_year", movie.release_year);
                li.addEventListener('click', movieSelected);
                classes.forEach(c => {
                    li.classList.add(c);
                })
                const li_content = document.createTextNode(`${movie.name} (${movie.release_year})`);
                li.appendChild(li_content);

                const ul = document.getElementById("result_list");
                ul.append(li);

            });
        });
});

document.getElementById("addmoviebtn").addEventListener('click', (event) => {
    search_input.focus()
    if (document.getElementsByClassName("searched_movie")) {
        document.getElementById("result_list").innerHTML = ""
        search_input.value = ""
    }
});

const save_list = document.getElementById("save-list");

if (save_list) {
    save_list.addEventListener("click", (event) => {
        list_items = document.getElementsByClassName("list-element");
        if (list_items.length === 0) {
            myAlert("list should have atleast one film");
            return;
        }
        if (document.getElementById("list_name").value.length === 0) {
            myAlert("list name is missing !");
            return;
        }
        const data = [{
            list_name: document.getElementById("list_name").value,
            list_desc: document.getElementById("list_desc").value
        }];


        Array.from(list_items).forEach(item => {
            data.push({
                tmdb_id: item.dataset.id,
                title: item.dataset.title,
                poster_path: item.dataset.poster_path,
                release_year: item.dataset.release_year,
            });
        });
        options.body = JSON.stringify(data);
        fetch("/lists/post", options).then(res => res.json())
            .then(res => {
                myAlert(res.message);
            })
    });
};

const update_list = document.getElementById("update-list");

if (update_list) {
    console.log("hello")
    update_list.addEventListener("click", event => {
        let list_name = document.getElementById("list_name").getAttribute("placeholder")
        let list_description = document.getElementById("list_desc").getAttribute("placeholder")

        if (document.getElementById("list_name").value.length !== 0) {
            list_name = document.getElementById("list_name").value;
        }
        if (document.getElementById("list_desc").value.length !== 0) {
            list_description = document.getElementById("list_desc").value;
        }

        const list_items = document.getElementsByClassName("list-element");
        if (list_items.length === 0) {
            myAlert("alteast need one film in list");
            return;
        }
        const data = [{
            id: document.getElementById("list_name").dataset.id,
            list_name: list_name,
            list_desc: list_description,
        }];
        Array.from(list_items).forEach(item => {
            data.push({
                tmdb_id: item.dataset.id,
                title: item.dataset.title,
                poster_path: item.dataset.poster_path,
                release_year: item.dataset.release_year,
            });
        });
        console.log(data);
        options.body = JSON.stringify(data);
        fetch("/lists/update", options).then(res => res.json())
            .then(res => {
                myAlert(res.message);
            })
    });
}