SID_FILE=$1
SUBTUNE=${2:-0} 
echo "Piping $SID_FILE (subtune $SUBTUNE) to sox"

./sidparse/sidparse "$SID_FILE" -a$SUBTUNE -b -t3000 | resid/pipe_dream 2>/dev/null | sox -traw -r44100 -b16 -c 1 -e signed-integer - -tcoreaudio
