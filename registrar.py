from rich.console import Console
import typer

app = typer.Typer()
console = Console()

# for this to work, need to use zsh terminal with python3 server.py COMMAND NAME
@app.command()
def add_student():
    console.print("Adding a new student...")

@app.command()
def add_course():
    console.print("Adding a new course...")

if __name__ == "__main__": app()