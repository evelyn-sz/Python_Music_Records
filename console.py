import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("David Gilmour")
artist_repository.add_to_library(artist_1)

artist_2 = Artist("Tony Anderson")
artist_repository.add_to_library(artist_2)

album_1 = Album("Rattle That Lock", "Rock", artist_1)
album_repository.add_to_library(album_1)

album_2 = Album("Spiriteaux", "Cinematic", artist_2)
album_repository.add_to_library(album_2)

artist_repository.select_all()

pdb.set_trace()