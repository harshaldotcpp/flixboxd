

function outlineConfirmPasswordBox(color,confirmPassword){
    
    const RED_COLOR_BORDER = "border-letterboxd-5";
    const GREEN_COLOR_BORDER = "border-letterboxd-4";
    let borderColorClass = "";
    
    if(color === "red"){
        borderColorClass = RED_COLOR_BORDER;
        confirmPassword.classList.remove("border-2",GREEN_COLOR_BORDER);
    }
    else if(color === "green"){
        borderColorClass = GREEN_COLOR_BORDER;
        confirmPassword.classList.remove("border-2",RED_COLOR_BORDER);
    } 
    
  

    confirmPassword.classList.add("border-2",borderColorClass);
    return;
}


function confirmPasswordIndicate(typed, campared){
    
    if(typed.value !== campared.value){
        outlineConfirmPasswordBox("red", campared);
        return false;
    }
    
    outlineConfirmPasswordBox("green",campared);
    return true;
}




function confirmPasswordIndicator(password,confirm_password){
    
    
    if(!confirmPasswordIndicate(password,confirm_password)){
        document.querySelector("#signup-btn").disabled = true;
        document.querySelector("#signup-btn").classList.remove("hover:bg-letterboxd-5", "bg-letterboxd-4");
        document.querySelector("#signup-btn").classList.add("bg-gray-900"); 
        return;
    };
    
    document.querySelector("#signup-btn").disabled = false;
    document.querySelector("#signup-btn").classList.remove("bg-gray-900");
    document.querySelector("#signup-btn").classList.add("hover:bg-letterboxd-5", "bg-letterboxd-4");

}

function validateForm(email,first_name,last_name,username,password){
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)+$/;
    
    if(!email.match(mailformat)){
        myAlert("Enter Valid Email");
        return false;
    }
    
    if(first_name.length === 0){
        myAlert("Name Missing");
        return false;
    }
    
    if(last_name.length === 0){
        myAlert("last Name Missin");
        return false;
    }
    
    if(username.length === 0){
        myAlert("Username Missing");
        return false;
    }
    
    if(password.includes(" ")){
        myAlert("Whitespace's not allowed in password"); 
        return false;
    }
    
    if(password.length < 7){
        myAlert("Password Must Contain More than Six Characters");
        return false;
    } 
    
    return true;
}



document.querySelector("#password").addEventListener("input",(event)=>{
    
    
    const confirm_password = document.querySelector("#confirm_password");
    confirmPasswordIndicator(event.currentTarget,confirm_password);
    

});

document.querySelector("#confirm_password").addEventListener("input",(event)=>{
    
    const password = document.querySelector("#password");
 
    confirmPasswordIndicator(password,event.currentTarget);

   
});



document.querySelector("#signup-form").addEventListener("submit",(event)=>{ 
    const email = document.querySelector("#email").value;
    const first_name = document.querySelector("#first_name").value;
    const last_name = document.querySelector("#last_name").value
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
    if(!validateForm(email,first_name,last_name,username,password.value))
        event.preventDefault();
        return;
        
    return;
});
