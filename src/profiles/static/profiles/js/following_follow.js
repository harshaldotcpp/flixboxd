const follow_btns = document.getElementsByClassName("follow")
Array.from(follow_btns).forEach(follow_btn => {
    follow_btn.addEventListener("click", (event) => {
        options.body = JSON.stringify({
            follow: follow_btn.checked,
        });
        let profile_username = event.target.dataset.username
        const icon = document.getElementById("icon-" + event.target.id)
        icon.classList.toggle("fill-letterboxd-4");
        let username = getCookie('username');
        const url = `/${username}/follow/` + profile_username;
        fetch(url, options);
    });
});