from pyscript import document, display

def sign_up(e):
    username = document.getElementById("user").value
    password = document.getElementById("pass").value   
    output = document.getElementById("output")

    if len(username) < 8:
        output.innerText = "User must contain at least 8 characters."
        return
    
    if len(password) < 10:
        output.innerText = "Password must contain at least 10 characters."
        return
    
    if not any(char.isalpha() for char in password):
        output.innerText = "Password must contain at least one letter."
        return
    
    if not any(char.isdigit() for char in password):
        output.innerText = "Password must contain at least one number."
        return
    
    else:
        output.innerText = "Account created successfully!"
