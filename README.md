# SIDler: ffmpeg for SID music

SIDler decodes and executes Commodore 64 subprograms for the SID.
An extension to siddump ("sidparse") is used to extract SID instruction as binary stream.
These binary instruction can be piped to an extension of resid ("pipedream") for rendering audio.

Obtaining a structured stream of binary instructions opens up many ways to resample/generate and otherwise learn from many SID tunes.
Such work is tbd with a layer of python.

## Requirements
- siddump/sidparse (see git submodle)
- resid/pipedream (see git submodule)
- sox (for cross platofrm audio out via bash)


## Usage: bash
./sidler-play <FOO.sid> <subtune (0-4);default 0>


## Usage: python
[TBD]
