from adventure.utils import read_events_from_file
from rich import print
import random

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[black on white]You stand still, unsure what to do.[/] [black on red] The forest swallows you.[/]"

def left_path(event):
    return "[black on white]You walk left.[/] " + event

def right_path(event):
    return "[black on white]You walk right.[/] " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[black on white]You wake up in a dark forest. You can go left or right.[/]")
    while True:
        choice = input("Which direction do you choose? (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("[black on white]Goodbye![/]")
            break
        
        print(step(choice, events))
