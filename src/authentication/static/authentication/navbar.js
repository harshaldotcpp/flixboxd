console.log("hello")
 const login_btn = document.querySelector("#signin_btn");
        const login_field = document.querySelector("#signin_menu");
        const search_btn = document.querySelector("#search_btn");
        const search_field = document.querySelector("#search_feild");
        const menu_btn = document.querySelector("#options_btn");
        const menu_field = document.querySelector("#menu_field");
        const signup_btn = document.querySelectorAll(".signup-btn");
        const signup_field = document.querySelector("#signup");
        
        
        //for login
        login_btn.addEventListener('click',(event)=>{
            
            if(menu_field.classList.contains("h-56")){
                menu_field.classList.toggle("h-56");
                menu_field.classList.toggle("h-0");
            }
                
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
                
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
                
            login_field.classList.toggle("hidden");
            login_field.classList.toggle("shadow-lg");
            login_field.classList.toggle("shadow-black");
        
        });
 
    
    
  

        //for search
        search_btn.addEventListener('click',(event)=>{
            
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
            
            if(menu_field.classList.contains("h-56")){
                menu_field.classList.toggle("h-56");
                menu_field.classList.toggle("h-0");
            }
            
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
                
            search_field.classList.toggle("hidden");
            search_field.classList.toggle("shadow-lg");
            search_field.classList.toggle("shadow-black");
        
        
        });
  
    
        //for menu
        menu_btn.addEventListener('click',(event)=>{
            if(!login_field.classList.contains("hidden"))
                login_field.classList.toggle("hidden");
            
            
            if(!search_field.classList.contains("hidden"))
                search_field.classList.toggle("hidden");
            
            if(!signup_field.classList.contains("hidden"))
                signup_field.classList.toggle("hidden");
            
            console.log(menu_field)
            menu_field.classList.toggle("h-56");
            menu_field.classList.toggle("h-0");
            menu_field.classList.toggle("shadow-lg");
            menu_field.classList.toggle("shadow-black");
        
 
        
        });
        
        signup_btn.forEach((btn)=>{
            btn.addEventListener("click",(event)=>{
                
                if(!login_field.classList.contains("hidden"))
                    login_field.classList.toggle("hidden");
           
                
                if(menu_field.classList.contains("h-56")){
                    menu_field.classList.toggle("h-56");
                    menu_field.classList.toggle("h-0");
                }
                
                if(!search_field.classList.contains("hidden"))
                    search_field.classList.toggle("hidden");
                
                signup_field.classList.toggle("hidden");
               
        
            });
        });