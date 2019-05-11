# SIDler: ffmpeg for SID music

SIDler decodes and executes Commodore 64 subprograms for the SID.
An extension to siddump ("sidparse") is used to extract SID instruction as binary stream.
These binary instruction can be piped to an extension of resid ("pipedream") for rendering audio.

Obtaining a structured stream of binary instructions opens up many ways to resample/generate and otherwise learn from many SID tunes.
Such work is tbd with a layer of python.

## Requirements
- gcc
- g++
- sox (for cross platform audio out via bash)

On Mac OS, `xcode-select --install` sets you up with compilers. Also, `brew install sox` sets you up with sox.


## Build
```
git clone https://github.com/ahirner/SIDler.git --recursive
cd SIDler
./build.sh
```

## Usage: bash
`./sidler-play.sh <FOO.sid> <subtune (0-4);default 0>`


## Usage: python
[TBD]
