#!/bin/bash

echo "Building submodule: sidparse"
cd sidparse && ./build.sh && cd ..

echo "Building submodule: resid"
cd resid && ./build.sh && cd ..

