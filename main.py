
from pyscript import document, display

my_list = ["Pabale", "Suarez", "Decierto", "Lee", "Balajadia", "Santos", "Juan", "Dela Cruz"]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = ""

    for item in my_list:
        display(item, target="output")

def check_name(e):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = first + " " + last

    message = document.getElementById("message")
    is_invited = last in my_list

    message.innerHTML = (
        f"You're on the list, {full_name}! See you there."
        if is_invited
        else f"Looks like you're not here, {first}"
    )

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
