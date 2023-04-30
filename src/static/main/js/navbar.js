const observer = lozad(); // lazy loads elements with default selector as '.lozad'
observer.observe();


const login_btn = document.querySelector("#signin_btn");
const login_field = document.querySelector("#signin_menu");
const search_btn = document.querySelector("#search_btn");
const search_field = document.querySelector("#search_feild");
const menu_btn = document.querySelector("#options_btn");
const menu_field = document.querySelector("#menu_field");
const signup_btn = document.querySelectorAll(".signup-btn");
const signup_field = document.querySelector("#signup");
const navbar = document.querySelector("nav");
const alert_ = document.querySelector("#alert");
const alert_btn = document.querySelector("#alert-btn");
const search_content_btn = document.querySelector("#search_content_btn")
const frontend_alert_btn = document.querySelector("frontend-alert-btn");


function windowClose(window) {
    if (window.classList.contains("hidden")){
        return true;
    }
    return false;
}

function windowOpen(window) {
    if (!window.classList.contains("hidden")){
        return true;
    }
    return false;
}

function closeWindow(window) {
    window.classList.add("hidden");
}

function openWindow(window) {
    window.classList.remove("hidden");
}

//for login
if (login_field) {

    login_btn.addEventListener('click', (event) => {
        if (windowOpen(menu_field)) {
            closeWindow(menu_field);
        }

        if (!search_field.classList.contains("hidden")){
            search_field.classList.toggle("hidden");
        }

        if (signup_field) {
            if (!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");

        }



        login_field.classList.toggle("hidden");
        navbar.classList.toggle("shadow-lg");
        navbar.classList.toggle("shadow-black");

    });
}




//for search
search_btn.addEventListener('click', (event) => {

    let should_toggle = true;
    if (login_field) {
        if (windowOpen(login_field)) {
            closeWindow(login_field);
            should_toggle = false;
        }
    }

    if (windowOpen(menu_field)) {
        closeWindow(menu_field);
        should_toggle = false;
    }
    if (signup_field) {
        if (windowOpen(signup_field)) {
            closeWindow(signup_field);
            should_toggle = false;
        }
    }

    search_field.classList.toggle("hidden");
    if (should_toggle) {
        navbar.classList.toggle("shadow-lg");
        navbar.classList.toggle("shadow-black");

    }


});


//for menu
menu_btn.addEventListener('click', (event) => {
    let should_toggle = true;
    if (login_field) {
        if (windowOpen(login_field)) {
            closeWindow(login_field);
            should_toggle = false;
        }
    }


    if (windowOpen(search_field)) {
        closeWindow(search_field);
        should_toggle = false;
    }

    if (signup_field) {
        if (windowOpen(signup_field)) {
            closeWindow(signup_btn);
            should_toggle = false;
        }
    }

    menu_field.classList.toggle("hidden");
    if (should_toggle) {
        navbar.classList.toggle("shadow-lg");
        navbar.classList.toggle("shadow-black");
    }



});
if (signup_field) {
    signup_btn.forEach((btn) => {
        btn.addEventListener("click", (event) => {
            if (login_field) {
                if (windowOpen(login_field))
                    closeWindow(login_field);
            }


            if (windowOpen(menu_field)) {
                closeWindow(menu_field);
            }

            if (windowOpen(search_field))
                closeWindow(search_field)

            signup_field.classList.toggle("hidden");


        });
    });
}
if (alert_) {

    setTimeout(() => {
        alert_.classList.add("hidden");
    }, 2000);
}
if (frontend_alert_btn) {
    frontend_alert_btn.addEventListener("click", (event) => {
        document.querySelector("#frontend-alert").classList.toggle("hidden");
    });
}

search_content_btn.addEventListener("click", (event) => {
    const content = document.querySelector("#search_content").value;
    if (content.length === 0) {
        document.querySelector("#alert-msg").innerHTML = "you forgot to type movie name lol";

        document.querySelector("#frontend-alert").classList.remove("hidden");
        setTimeout(() => {
            document.querySelector("#frontend-alert").classList.add("hidden");
        }, 1300);
        return;
    }
    const action_url = "/film/search/" + content;
    location.href = action_url;
});


desktop_signin = document.getElementById("desktop-signin");
if (desktop_signin) {
    desktop_signin.addEventListener("click", (event) => {
        const desktop_signin_form = document.getElementById("desktop-signin-form");
        desktop_signin_form.classList.remove("hidden");

        const navbar = document.getElementById("main-navbar");
        navbar.classList.add("opacity-0");
    });


}

desktop_signin_form_cancel = document.getElementById("desktop-sigin-form-cancel");
if (desktop_signin_form_cancel) {
    desktop_signin_form_cancel.addEventListener("click", (event) => {
        desktop_signin_form = document.getElementById("desktop-signin-form");
        desktop_signin_form.classList.toggle("hidden");
        navbar.classList.remove("opacity-0");
    });
};


desktop_profile_menu = document.getElementById("desktop-profile-menu")

if(desktop_profile_menu){
    desktop_profile_menu.addEventListener("mouseover",(event)=>{
        desktop_profile_menu.classList.add("bg-letterboxd-3");
        extend_menu = document.getElementById("desktop-profile-menu-extend");
        extend_menu.classList.remove("hidden");
    });
}
if(desktop_profile_menu){
    desktop_profile_menu.addEventListener("mouseout",(event)=>{
        desktop_profile_menu.classList.remove("bg-letterboxd-3");
        extend_menu.classList.add("hidden");
    });
}