#!venv/bin/python
from youtubesearchpython import *
import os
from rich.console import Console


os.system('clear')
console = Console()
console.print("Enter a song name ",style="blink bold cyan")
search = input()
videos_search = VideosSearch(query=search,limit=10)

i=1

for video in videos_search.result()['result']:
    title = video['title']
    link =  video['link']
    if(i%2==0):
        console.print(f"[[red]{i}[/red]] [bold magenta]{title}")
    else:
        console.print(f"[[red]{i}[/red]] [bold green]{title}")   
    i+=1
console.print(f"Enter a selection 1-{i-1} ",style="bold yellow")
s = int(input()) 
while not (s>=1 and s<=i):
    console.print("Invalid input",style="bold red")   
    console.print("Enter a song name: ",style="bold green")
    s = int(input()) 
ll = videos_search.result()['result'][s-1]['link']
console.print("Playing.....",style="blink2 italic red ")
os.system(f"mpv {ll} --no-video --no-audio-display")






# print(audio)
# time.sleep(110)