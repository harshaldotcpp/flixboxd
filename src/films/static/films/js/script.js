        const watch_btn = document.querySelector("#watch-btn");
        const like_btn = document.querySelector("#like_btn");
        const watchlist_btn = document.querySelector("#watchlist_btn");
        const review_btn = document.querySelector("#review-btn");
        const review_cancel_btn = document.querySelector("#review-cancel-btn");
        var date = new Date();
        
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        
        if (month < 10) month = "0" + month;
        if (day < 10) day = "0" + day;
        
        var today = year + "-" + month + "-" + day;  
        
        
        
        
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
        
        document.getElementById('datePicker').value = today;
        document.getElementById('datePicker').ariaPlaceholder = today;

        review_btn.addEventListener("click",(event)=>{
            document.getElementById("movie-review-log").classList.toggle("hidden");
        });

        review_cancel_btn.addEventListener("click", event =>{
            document.getElementById("movie-review-log").classList.toggle("hidden")
        });


        watch_btn.addEventListener("click",(event)=>{
            console.log("watch_btn ");
            const icon = document.querySelector("#watch-icon");
            icon.classList.toggle("fill-letterboxd-4");
           console.log("im in")
            if(!watch_btn.checked && like_btn.checked){
                console.log("in if")
                const icon = document.querySelector("#like-icon");
                icon.classList.toggle("fill-letterboxd-5")
                like_btn.checked = false;
            }


            if(watch_btn.checked && watchlist_btn.checked){
                const icon = document.querySelector("#watchlist-icon");
                icon.classList.toggle("fill-letterboxd-4");
                watchlist_btn.checked = false;
            }

            options.body = JSON.stringify({ 
                add: watch_btn.checked,
                tmdb_id: getCookie('id'),
                title: getCookie('movie_name'),
                poster_path: getCookie('poster_path'),
                director: getCookie('director'),
                
             });
            
           
            fetch("http://localhost:8000/film/watchedadd",options)
             
        });
        
        like_btn.addEventListener("click",(event)=>{
            console.log(" played");
                const icon = document.querySelector("#like-icon");
                icon.classList.toggle("fill-letterboxd-5");
                
                //if film liked and unwatched mark as watched liking movie also add into watched
                if(like_btn.checked && !watch_btn.checked){
                    
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
               
                fetch("http://localhost:8000/film/likedadd",options)
       
        });
        
        watchlist_btn.addEventListener("click",(event)=>{
            console.log("watchlist played");
            const icon = document.querySelector("#watchlist-icon");
            icon.classList.toggle("fill-letterboxd-4");
            options.body = JSON.stringify({ 
                    add: watchlist_btn.checked,
                    tmdb_id: getCookie('id'),
                    title: getCookie('movie_name'),
                    poster_path: getCookie('poster_path'),
                    director: getCookie('director'),
                });

                fetch("http://localhost:8000/film/watchlistadd",options)
        });

        document.querySelector("#maction").addEventListener("click",()=>{
            document.querySelector("#movie-add").classList.toggle("hidden");
        })