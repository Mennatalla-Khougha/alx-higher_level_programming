#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    for c in names:
        if c startwith('__'):
            continue
        print(f'{c}')
