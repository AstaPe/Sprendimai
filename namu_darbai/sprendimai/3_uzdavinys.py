from namu_darbai.classes.playlist3 import Playlist

my_playlist = Playlist()

my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")


my_playlist.remove_song("Song 2")


print("Visos dainos grojaraštyje:", my_playlist.list_songs())
