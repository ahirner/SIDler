from typing import NamedTuple


class Header(NamedTuple):
    filetype: str
    version: int

    data_offset: int
    play_address: int
    load_address: int
    init_address: int
    song_numbers: int
    default_song: int
    speed: int          # 0 == 50hz vertical blank, else CIA Timer

    title: str
    author: str
    released: str
