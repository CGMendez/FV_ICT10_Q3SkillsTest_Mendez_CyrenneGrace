from pyscript import document, display

# Function that runs when the Sign Up button is clicked
def sign_up(event):

    # Get the username value from input field
    username = document.getElementById("user").value

    # Get the password value from input field
    password = document.getElementById("pass").value

    # Get the paragraph where messages will be displayed
    output = document.getElementById("output")

    # Create an empty list to store validation messages
    messages = []

    # Check if username has less than 8 characters
    if len(username) < 8:
        missing_user = 8 - len(username)
        messages.append(f"Username needs {missing_user} more character(s).")

    # Check if password has less than 10 characters
    if len(password) < 10:
        missing_pass = 10 - len(password)
        messages.append(f"Password needs {missing_pass} more character(s).")

    # Check if password contains at least one letter
    if not any(char.isalpha() for char in password):
        messages.append("Password needs at least 1 letter.")

    # Check if password contains at least one number
    if not any(char.isdigit() for char in password):
        messages.append("Password needs at least 1 number.")

    # If there are validation errors
    if messages:
        output.innerHTML = "<br>".join(messages)
    else:
        # If all conditions are satisfied
        output.innerText = "Account created successfully!"

