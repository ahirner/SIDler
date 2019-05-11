"""
Reading and parsing info from SID files
"""

from typing import Union
import logging
import io

from schema import Header


def decode_c_str(b: bytes) -> str:

    s = b.split(b'\0', 1)[0].decode('ascii', errors='ignore')
    return s

def extract_header(file: Union[io.BytesIO, str]) -> Header:

    if isinstance(file, str):
        file = open(file, "rb")

    file.seek(0)
    data = file.read(119)
    if len(data) < 119:
        raise ValueError("Two few bytes (%d) for SID header" % len(data))

    filetype = data[0:4].decode()
    version = data[5]

    logging.debug(f"SID type: {filetype} (version {version})")
    if filetype == "RSID":
        logging.warning("RSID files may not play properly. YMMV.")

    data_offset = (data[6] << 8) | data[7]
    logging.debug("Data offset:  {0:04X}".format(data_offset))
    load_address = (data[8] << 8) | data[9]
    logging.debug("Load address: {0:04X}".format(load_address))
    init_address = (data[10] << 8) | data[11]
    logging.debug("Init address: {0:04X}".format(init_address))
    play_address = (data[12] << 8) | data[13]
    logging.debug("Play address: {0:04X}".format(play_address))

    song_numbers = (data[14] << 8) | data[15]
    default_song = (data[16] << 8) | data[17]
    logging.debug(f"Found {song_numbers} song(s) "
                  f"(default song is {default_song})")

    speed = (data[18] << 24) | (data[19] << 16) | (data[20] << 8) | data[21]
    if speed == 0:
        logging.debug("Using 50Hz vertical blank interrupt.")
    else:
        logging.warning("Some songs require the CIA 1 timer (not implemented).")

    title = decode_c_str(data[22:54])
    author = decode_c_str(data[54:86])
    released = decode_c_str(data[86:118])

    logging.debug(f"Title    : {title}")
    logging.debug(f"Author   : {author}")
    logging.debug(f"released : {released}")

    ## Check load address
    if load_address == 0:
        logging.warning("SID has load address 0, reading from C64 binary data")
        file.seek(data_offset)
        data = file.read(2)
        load_address = data[0] | (data[1] << 8)
        # load_bytes = 2
        logging.debug("New load address is {0:04X}".format(load_address))

    ## Check init address
    if init_address == 0:
        logging.warning("SID has init address 0, cloning load address instead")
        init_address = load_address
        logging.debug("New init address is {0:04X}".format(init_address))

    # We assume init is everything before play, so don't remember these
    # sequences, otherwise we can grep this code as follows:
    # init_seq = data[initaddress-loadaddress:playaddress-loadaddress]
    # Add skipped code from offset to init
    # skipped_seq = data[dataoffset+load_bytes:initaddress-loadaddress]

    return Header(filetype, version, data_offset, play_address, load_address,
                  init_address, song_numbers, default_song, speed, title, author,
                  released)
