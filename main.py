import requests
import random
import os

def main():
    if not os.path.exists('OsuSong'):
        os.makedirs('OsuSong')
    
    min_star = float(input('Enter the minimum star rating: '))
    max_star = float(input('Enter the maximum star rating: '))
    print(f'Downloading, please be patient (This can take some time)')
    
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
            
        if star_rating < min_star or star_rating > max_star:
            continue

        song_name = song_name.replace(".", "_")
        star_rating = f"{star_rating}".replace(".","")

        # Check if file already exists
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

            print(f"Downloaded: {filename1} in OsuSong Folder")

        except:
            pass

if __name__ == '__main__':
    main()
