import os

def main():
    files = os.listdir('OsuSong')

    files.sort(key=lambda x: os.path.getmtime(os.path.join('OsuSong', x)), reverse=True)

    for file in files:
        file_path = os.path.join('OsuSong', file)
        os.startfile(file_path)

if __name__ == '__main__':
    main()
