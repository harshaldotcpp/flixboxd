

function outlineConfirmPasswordBox(color,confirmPassword){
    
    let borderColorClass = "";
    switch(color){
        case "red": borderColorClass = "border-red-900";
                   break;
        case "green": borderColorClass = "border-green-900";
                    break;
                    
    }
    confirmPassword.classList.add("border-2",borderColorClass);
    return;
}

function confirmPassword(password, confirmPassword){
    
    if(password.value !== confirmPassword.value){
        outlineConfirmPasswordBox("red", confirmPassword);
        return;
    }
    
    markConfirmPasswordBox("green",confirmPassword);
    return;
}


