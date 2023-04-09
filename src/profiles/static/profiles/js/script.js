const follow_btn = document.getElementById("follow-btn")


if(follow_btn){
follow_btn.addEventListener("click", (event) => {
    const follow_btn_text = document.getElementById("follow-btn-text")

    if (follow_btn.checked)
        follow_btn_text.innerHTML = "unfollow"
    else
        follow_btn_text.innerHTML = "follow"

    options.body = JSON.stringify({
        follow: follow_btn.checked,
    });
    let username = getCookie('username');

    const url = "/profile/follow/" + username;
    fetch(url,options);


})
}