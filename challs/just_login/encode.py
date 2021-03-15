key = 0x55
with open('flag.txt', 'rb') as f:
    print('{' + ', '.join(map(lambda x: str(x^key), f.readline().strip())) + '}')
