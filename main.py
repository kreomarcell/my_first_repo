if __name__ == '__main__':

    with open('data.txt', 'rb') as file:
        data = file.read()
    print('            00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f')
    for i in range(0, len(data), 16):
        addr = f'{hex(i // 16 * 16)[2:]:0>8}'
        hx = ' '.join(f'{hex(el)[2:]:0>2}' for el in data[i:i + 16])
        s = ''.join(chr(el) if chr(el).isprintable() else '.' for el in data[i:i + 16])
        print(f'{addr}    {hx:<48}     {s}')

#  добавил комментарий