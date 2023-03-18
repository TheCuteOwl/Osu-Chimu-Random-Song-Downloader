import requests
import random
import os
def main():
    if not os.path.exists('OsuSong'):
        os.makedirs('OsuSong')

    star = input(str('Which star level you want to have (Like if you input 5 you will get 5 and some over 5) -> '))
    print('Downloading, Please be patient (This can take some time)')
    while True:
        random_number = str(random.randint(100000, 160000))
        url = f"https://api.chimu.moe/v1/download/{random_number}?n=1"

        beatmap_url = f"https://api.chimu.moe/v1/map/{random_number}"
        response = requests.get(beatmap_url)
        try:
            data = response.json()
            star_rating = data["DifficultyRating"]
            song_name = data["OsuFile"]
        except KeyError:
            continue

        if star_rating < float(star):
            continue

        song_name = song_name.replace(".", "_")
        star_rating = f"{star_rating}".replace(".","")
        # Check if file already exists
        filename1 = f"{star_rating} Apophis {song_name}.osz"
        if os.path.isfile(os.path.join('OsuSong', filename1)):
            continue

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() # raise an error for non-200 status codes
            filename2 = os.path.join('OsuSong', filename1)
            with open(filename2, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print(f"Downloaded: {filename1} in OsuSong Folder")

        except:
            pass

main()
