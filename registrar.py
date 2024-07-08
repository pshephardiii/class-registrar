from rich.console import Console
import typer
from server import reset, add_a_student

app = typer.Typer()
console = Console()

# for this to work, need to use zsh terminal with python3 server.py COMMAND NAME
# to add student, type "python3 registrar.py add-student FIRST LAST UNIX-ID" where all caps should be replaced with values
@app.command()
def add_student(first_name: str, last_name: str, unix_id: str):
    add_a_student(first_name, last_name, unix_id)
    console.print("Adding a new student!")

@app.command()
def add_course():
    console.print("Adding a new course...")

@app.command()
def reset_database():
    answer = input("This will delete all the data.  Are you sure? (y/n): ")

    if answer.strip().lower() == "y":
        reset()
        console.print("Database reset successfully")
    else:
        console.print("Database reset aborted")
    

if __name__ == "__main__": app()