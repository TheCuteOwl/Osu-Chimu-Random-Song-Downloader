import requests
import random
import os, sys, subprocess
import Launchall
from Launchall import main
import shutil
import colorama
from colorama import Fore, init
colorama.init()



def clear_console():
    if sys.platform.startswith('win'):
        _ = subprocess.call('cls', shell=True)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        _ = subprocess.call('clear', shell=True)
    else:
        print('Unsupported platform. Cannot clear console.')

def set_terminal_title(title):
        if sys.platform.startswith('linux'):
            sys.stdout.write(f"\x1b]2;{title}\x07")
        elif sys.platform.startswith('darwin'):
            sys.stdout.write(f"\033]0;{title}\007")
        elif sys.platform.startswith('win'):
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            raise ValueError("Unsupported platform")
        

def print_centered(text):
    console_width, _ = shutil.get_terminal_size()
    padding = (console_width - len(text)) // 2
    print(' ' * padding + text)

def input_centered(prompt):
    console_width, _ = shutil.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input

Red = Fore.RED
Blue = Fore.BLUE
Green = Fore.GREEN
Yellow = Fore.YELLOW
Reset = Fore.RESET

Debug = ''
def end():
    clear_console()
    Choice = input_centered(f'''{Green}Installed{Reset}, Do you want to {Green}import{Reset} all the maps on {Green}Osu!{Reset} ?
          [{Green}1{Reset}] {Green}Yes{Reset} ({Green}Will{Reset} import and after that Quit)({Red}Epileptical{Reset} warning)
          [{Green}2{Reset}] {Green}No{Reset} ({Green}Quit{Reset})
          ->''')
    if Choice == '1':
        Launch()
        quit()
    else:
        quit()

def Launch():
        files = os.listdir('OsuSong')

        files.sort(key=lambda x: os.path.getmtime(os.path.join('OsuSong', x)), reverse=True)

        for file in files:
            file_path = os.path.join('OsuSong', file)
            os.startfile(file_path)

            print(f'{Green}Started{Reset} {file_path}')

def main():
    if not os.path.exists('OsuSong'):
        os.makedirs('OsuSong')
    print_centered(f'{Red}Warning{Reset}, Because of downloading random map, it may be able to download very {Red}bad{Reset} song with ({Red}P*rn{Reset}, {Red}Horror{Reset} and other Be {Red}AWARE{Reset}')
    min_star = float(input_centered(f'Enter the minimum {Yellow}star{Reset} rating: '))
    max_star = float(input_centered(f'Enter the maximum {Yellow}star{Reset} rating: '))
    First = int(input_centered(f'How many songs do you want to {Yellow}download?{Reset} '))
    Debug = input_centered(f"""Do you want to get more {Yellow}information{Reset} (Beatmaps that's are not downloaded and some other stuff\n
    
    
    [{Yellow}1{Reset}] {Yellow}Yes{Reset}
    [{Yellow}2{Reset}] {Yellow}No {Reset}
    ->""")

    if Debug == '1':
        Debug = 'True'
    else: Debug = 'False'
    Debug2 = ''
    if Debug == 'True':
        Debug2 = f"{Green}True"
    else:
        Debug2 = f"{Red}False"

    clear_console()
    print(f'Minimun {Yellow}star{Reset} : {Green}{min_star}{Reset}')
    print(f'Minimun {Yellow}star{Reset} : {Green}{max_star}{Reset}')
    print(f'Debug {Yellow}Mode{Reset} : {Debug2}\n\n')
    print_centered(f'{Yellow}Downloading{Reset}, please be {Yellow}patient{Reset} (This can take {Yellow}some{Reset} time)\n')
    Second = 0

    while True:
        if First == Second:
            end()
        else:
            pass
        random_number = str(random.randint(1, 200000))
        url = f"https://api.chimu.moe/v1/download/{random_number}?n=1"
        if Debug == 'True':
            print_centered(f'{Green}Generating{Reset} new link...')

        beatmap_url = f"https://api.chimu.moe/v1/map/{random_number}"
        response = requests.get(beatmap_url)

        if Debug == 'True':
            print_centered(f'Checking the {Green}Chimu-Moe API{Reset} if the map exist..')

        try:
            data = response.json()
            star_rating = data["DifficultyRating"]
            song_name = data["OsuFile"]
        except KeyError:
            continue
        if star_rating < min_star or star_rating > max_star:
            continue
        

        song_name = song_name.replace(".", "_")
        star_rating = f"{star_rating}".replace(".","")

        # Check if file already exists
        filename1 = f"{star_rating} TheCuteOwl-Github {song_name}.osz"
        if os.path.isfile(os.path.join('OsuSong', filename1)):
            continue

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() 
            filename2 = os.path.join('OsuSong', filename1)
            with open(filename2, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            if Debug == 'True':
                print_centered(f'{Green}Map founded{Reset}...')
            print_centered(f"{Yellow}Downloaded:{Reset} {filename1} in {Yellow}OsuSong Folder{Reset}")
            Second += 1
            if Debug == 'True':
                print_centered(f'{Green}{Second}/{First} Downloaded{Reset}...')
        except:
            pass


if __name__ == '__main__':
    main()
