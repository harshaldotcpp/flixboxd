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
        document.getElementById('datePicker').value = today;
        document.getElementById('datePicker').ariaPlaceholder = today;

        review_btn.addEventListener("click",(event)=>{
            document.getElementById("movie-review-log").classList.toggle("hidden");
        });

        review_cancel_btn.addEventListener("click", event =>{
            document.getElementById("movie-review-log").classList.toggle("hidden")
        });
        watch_btn.addEventListener("click",(event)=>{
            console.log("watch_btn played");
            const icon = document.querySelector("#watch-icon");
            icon.classList.toggle("fill-letterboxd-4");
        });
        like_btn.addEventListener("click",(event)=>{
            console.log("liked played");
                const icon = document.querySelector("#like-icon");
                icon.classList.toggle("fill-letterboxd-5");
        });
        watchlist_btn.addEventListener("click",(event)=>{
            console.log("watchlist played");
            const icon = document.querySelector("#watchlist-icon");
            icon.classList.toggle("fill-letterboxd-4");
        });

        document.querySelector("#maction").addEventListener("click",()=>{
            document.querySelector("#movie-add").classList.toggle("hidden");
        })