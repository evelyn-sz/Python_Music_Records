import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("Rattle That Lock", "Rock", "David Gilmour")

    def test_album_has_title(self):
        self.assertEqual("Rattle That Lock", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("David Gilmour", self.album.artist)