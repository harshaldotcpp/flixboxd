const search_input = document.getElementById("movie-search")


function movieSelected(){
    console.log("selected");
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
                const classes = ["hover:bg-letterboxd-4", "py-2", "px-2","searched_movie"];
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

document.getElementById("addmoviebtn").addEventListener('click',(event)=>{
    search_input.focus()
    if(document.getElementsByClassName("searched_movie")){
        document.getElementById("result_list").innerHTML = ""
        search_input.value = ""
    }
})