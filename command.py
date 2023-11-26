import rich_click
import pathlib
import json
import hashlib
from rich import print

session = pathlib.Path('./running/session.json')
session_content = json.loads(session.read_text()) if session.exists() else None

@rich_click.group()
def cli():
    pass

@cli.command()
@rich_click.argument('username', type=str)
@rich_click.argument('password', type=str)
def login(username: str, password: str):
    users = json.loads(pathlib.Path('./users.json').read_text('utf-8'))

    for user in users:
        if user['username'] == username and user['password_sha256'] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            if user['role'] == 'O5' or user['level'] == 5:
                print("[red r]Warning: Impersonating the O5 is to be [b]terminated immediately[b]. Your location has been locked; If you fail the biometric test, the MTF will be dispatched to your location within 4 minutes. Now place your palm over the vein validator.")
                print("[red]Pressing the Enter key means that you have completed the vein verification.")
                input()

            print("[cyan]Please waiting for creating session file on this terminal.")
            session.write_text(json.dumps(user))
            print("[green]Successed to create session file on this terminal. [red][b u]DO NOT[/b u] leave the terminal while you are logged in.")
            print(f"[green]Welcome to back [cyan b]{user['username']}")

@cli.command()
@rich_click.argument('order', type=str)
@rich_click.option('--language', default='en')
def read(order: str, language: str):
    print('reading')

if __name__ == "__main__":
    cli()
