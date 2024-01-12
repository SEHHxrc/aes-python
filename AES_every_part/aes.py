import sbox, add_round_key, diffusion


def scanf(keyword):
    if keyword == 'message':
        string = input('input your message:')
    else:
        string = input('input the key:')
    matrix = [[], [], [], []]
    s = string.split(' ')
    for i in range(len(s)):
        matrix[i % 4].append(int(s[i], 16))
    return matrix


def printf(m, mode=''):
    if mode == 'add_round_key':
        print(mode)
        for i in range(len(m)):
            for j in range(4):
                m[i][j] = hex(m[i][j])[2:]
        for k in m:
            print(k)
    else:
        s = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                s[i].append(hex(m[j][i])[2:])
        print(mode)
        for k in s:
            print(k)


if __name__ == '__main__':
    message = scanf('message')  # 32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34
    key = scanf('key')  # 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c
    printf(add_round_key.add_round_key(message, key), 'add_round_key')
    message = add_round_key.add_round_key(message, key)
    printf(sbox.sub_bytes(message, sbox.s_box), 'sub_bytes')
    message = sbox.sub_bytes(message, sbox.s_box)
    diffusion.shift_rows(message)
    printf(message, 'shift_rows')
    diffusion.mix_columns(message)
    printf(message, 'mix_columns')


