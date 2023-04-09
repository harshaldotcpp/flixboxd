// function to populate alerts
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

// for cookie request function
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

function getTodaysDate() {
    var date = new Date();

    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    if (month < 10) month = "0" + month;
    if (day < 10) day = "0" + day;

    return year + "-" + month + "-" + day;

}


const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    },
    mode: 'same-origin',
    body: "",
}