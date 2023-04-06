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



const follow_btn = document.getElementById("follow-btn")



follow_btn.addEventListener("click", (event) => {
    console.log(follow_btn.checked)
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