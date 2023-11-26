import os
import threading
import random
import time
from rich import color, print
from rich.progress import Progress, TaskID, TextColumn, BarColumn, TimeElapsedColumn
from typing import Optional

if __name__ == "__main__":
    print("[cyan] SCiPNet Version [red]SIGMA-12 [white]‖[green] build20231126")

    with Progress() as progress:
        for server in ['America Main Server', 'Asia Main Server', 'Europe Main Server', 'Oceania Main Server', 'Africa Main Server', 'Antarctica Main Server', 'Local Site Verification Server', 'Site-7 Cluster Control Plane']:
           p = progress.add_task(description=f'The terminal is connecting [cyan bold]{server}', total=5)
           
           for i in range(5):
               progress.advance(p)
               time.sleep(random.random() / 10)
    
    print("[r]Welcome to access SCiPNet. [u b]Please login.")

    while True:
        command = input("SCiPNet> ").split(" ")
        
        os.system(f"python command.py {' '.join(command)}")
