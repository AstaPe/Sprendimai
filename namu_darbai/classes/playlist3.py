class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f'Daina "{song}" pridėta į grojaraštį.')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Daina "{song}" pašalinta iš grojaraščio.')
        else:
            print(f'Daina "{song}" nerasta grojaraštyje.')

    def list_songs(self):
        return self.songs