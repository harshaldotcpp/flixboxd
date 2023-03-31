
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
      
       
        //for login
    if(login_btn){
        login_btn.addEventListener('click',(event)=>{
            
            if(!menu_field.classList.contains("hidden")){
                menu_field.classList.toggle("hidden");
            }
                
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
                
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
                
            login_field.classList.toggle("hidden");
            navbar.classList.toggle("shadow-lg");
            navbar.classList.toggle("shadow-black");
        
        });
    }
    
    
  

        //for search
        search_btn.addEventListener('click',(event)=>{
            
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
            
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
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
            
            
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
           
            if(signup_field){
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
            }
            console.log("hello")
            menu_field.classList.toggle("hidden");
            navbar.classList.toggle("shadow-lg");
            navbar.classList.toggle("shadow-black");
        
 
        
        });
       if(signup_field){
        signup_btn.forEach((btn)=>{
            btn.addEventListener("click",(event)=>{
                
                if(!login_field.classList.contains("hidden"))
                    login_field.classList.toggle("hidden");
           
                
                if(!menu_field.classList.contains("hidden")){
                    menu_field.classList.toggle("hidden");
              
                }
                
                if(!search_field.classList.contains("hidden"))
                    search_field.classList.toggle("hidden");
                
                signup_field.classList.toggle("hidden");
               
        
            });
        });
       }
    if(alert_btn){
            alert_btn.addEventListener("click",(event)=>{
            alert_.classList.toggle("hidden");
        });
    }
        
        