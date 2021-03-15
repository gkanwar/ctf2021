import struct

with open('flag.bmp', 'rb') as f:
    raw_bytes = f.read()
with open('flag.bin', 'wb') as f:
    off = struct.unpack('<I', raw_bytes[10:14])[0]
    f.write(raw_bytes[off:])
