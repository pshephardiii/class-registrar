from rich.console import Console
import typer
from server import reset
from server import get_connection

app = typer.Typer()
console = Console()

# for this to work, need to use zsh terminal with python3 server.py COMMAND NAME
@app.command()
def add_student():
    console.print("Adding a new student...")

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