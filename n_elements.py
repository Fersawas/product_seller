def long_string(n):
    res = []
    for i in range(1, n+1):
        res += [str(i)] * i
        if len(res) > n:
            break
    return ''.join(res[:n])


if __name__ == '__main__':
    print(long_string(int(input())))
