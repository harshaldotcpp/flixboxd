
 const login_btn = document.querySelector("#signin_btn");
        const login_field = document.querySelector("#signin_menu");
        const search_btn = document.querySelector("#search_btn");
        const search_field = document.querySelector("#search_feild");
        const menu_btn = document.querySelector("#options_btn");
        const menu_field = document.querySelector("#menu_field");
        const signup_btn = document.querySelectorAll(".signup-btn");
        const signup_field = document.querySelector("#signup");
        const navbar = document.querySelector("nav")
        const alert_ = document.querySelector("#alert");
        const alert_btn = document.querySelector("#alert-btn");
        const search_content_btn = document.querySelector("#search_content_btn")
        const frontend_alert_btn = document.querySelector("frontend-alert-btn");
       
        //for login
    if(login_field){
        console.log(login_btn)
        login_btn.addEventListener('click',(event)=>{
            if(!menu_field.classList.contains("hidden")){
                menu_field.classList.toggle("hidden");
            }
                
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
            
            if(signup_field){
                if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
             
            }
            

               
            login_field.classList.toggle("hidden");
            navbar.classList.toggle("shadow-lg");
            navbar.classList.toggle("shadow-black");
        
        });
    }
    
    
  

        //for search
        search_btn.addEventListener('click',(event)=>{
           if(login_field){ 
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
           }
            
            if(!menu_field.classList.contains("hidden")){
                menu_field.classList.toggle("hidden");
            }
            if(signup_field){
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
            } 
            search_field.classList.toggle("hidden");
            navbar.classList.toggle("shadow-lg");
            navbar.classList.toggle("shadow-black");
          
        
        });
  
    
        //for menu
        menu_btn.addEventListener('click',(event)=>{
            if(login_field){
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
            }
            
            
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
           
            if(signup_field){
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
            }
            
            menu_field.classList.toggle("hidden");
            navbar.classList.toggle("shadow-lg");
            navbar.classList.toggle("shadow-black");
        
 
        
        });
       if(signup_field){
        signup_btn.forEach((btn)=>{
            console.log("gello");
            btn.addEventListener("click",(event)=>{
               if(login_field){ 
                if(!login_field.classList.contains("hidden"))
                    login_field.classList.toggle("hidden");
               }
           
                
                if(!menu_field.classList.contains("hidden")){
                    menu_field.classList.toggle("hidden");
              
                }
                
                if(!search_field.classList.contains("hidden"))
                    search_field.classList.toggle("hidden");
                
                signup_field.classList.toggle("hidden");
               
        
            });
        });
       }
    if(alert_){

            setTimeout(()=>{
                alert_.classList.add("hidden")
            },1700);
            // alert_btn.addEventListener("click",(event)=>{
            //     alert_.classList.toggle("hidden");
            // });
    }
    if(frontend_alert_btn){
    frontend_alert_btn.addEventListener("click",(event)=>{
        document.querySelector("#frontend-alert").classList.toggle("hidden")
    })
    }
       
    search_content_btn.addEventListener("click",(event)=>{
        const content = document.querySelector("#search_content").value

        if(content.length === 0){
            document.querySelector("#alert-msg").innerHTML = "you forgot to type movie name lol";

            document.querySelector("#frontend-alert").classList.remove("hidden")
            setTimeout(()=>{
                document.querySelector("#frontend-alert").classList.add("hidden");
            },1300);
            return;
        }
        const action_url = "http://localhost:8000/search/film/" + content;
        location.href = action_url
    });
        