import requests
import random
import os
import Launchall
from Launchall import main
def end():
    Choice = input('''Installed, Do you want to import all the maps on osu?
          [1] Yes (Will import and after that Quit) (You need to have osu already launched)
          [2] No (Quit)
          ->''')
    if Choice == '1':
        Launchall.main()
        quit()
    else:
        quit()


def main():
    if not os.path.exists('OsuSong'):
        os.makedirs('OsuSong')
    
    min_star = float(input('Enter the minimum star rating: '))
    max_star = float(input('Enter the maximum star rating: '))
    First = int(input('How many songs do you want to install? '))
    Debug = input("""Do you want to get more information (Beatmaps that's are not downloaded and some other stuff)*
    
    [1] Yes
    [2] No 
    ->""")
    print('Downloading, please be patient (This can take some time)')
    Second = 0

    while True:
        if First == Second:
            end()
        else:
            pass
        random_number = str(random.randint(100000, 160000))
        url = f"https://api.chimu.moe/v1/download/{random_number}?n=1"
        if Debug == '1':
            print('Generate new link...')

        beatmap_url = f"https://api.chimu.moe/v1/map/{random_number}"
        response = requests.get(beatmap_url)

        if Debug == '1':
            print('Checking the API if the map exist..')

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

        filename1 = f"{star_rating} Apophis {song_name}.osz"
        if os.path.isfile(os.path.join('OsuSong', filename1)):
            continue

        try:
            response = requests.get(url, stream=True)
            if Debug == '1':
                print('Map founded...')
            response.raise_for_status() 
            filename2 = os.path.join('OsuSong', filename1)
            with open(filename2, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print(f"Downloaded: {filename1} in OsuSong Folder")
            Second += 1

        except:
            pass

if __name__ == '__main__':
    main()
