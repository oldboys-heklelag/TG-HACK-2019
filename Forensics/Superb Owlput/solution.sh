# The very first packets in the file look like DNS tunneling
# In wireshark: Clicking statistics > Conversations and listing IPv4 conversations by bytes transferred reveals a huge number of bytes(compared to other conversations)
# between two hosts. Filtering this out: (ip.addr==172.19.0.3 && ip.addr==172.19.1.50) && (dns.flags == 0x0100)
# and store all the packets as a new file. We can then extract the data partof the queries with tcpdump:
sudo tcpdump -nnr tunnel.pcap | awk '{print $8}' | cut -f 1 -d '.' >> hexfile

# Removing the whitespace:
cat hexfile | tr -d " \t\n\r" > hexfile2

# Observing the magic numbers (By inputing the start of the file into cyberchef - magic for instance) reveals that this should be a jpeg image:
xxd -r -p hexfile2 flag.jpg

# The image itself is not too interesting, but viewing the EXIF data reveals a strange-looking author.
# Decoding this as base64 reveals the flag
identify -verbose flag.jpg | grep "exif:Artist" | awk '{print $2}' | base64 -d
