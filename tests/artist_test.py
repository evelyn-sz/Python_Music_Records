import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("David Gilmour")

    def test_artist_has_name(self):
        self.assertEqual("David Gilmour", self.artist.name)