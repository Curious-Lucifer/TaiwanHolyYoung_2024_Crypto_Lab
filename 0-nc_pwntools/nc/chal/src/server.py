import sys

from secret import FLAG

def repeat(word):
    print(f'CuriousGPT > {word}')
    if input('> ') != word:
        print('Error : wrong word')
        sys.exit()

def main():
    print('Description : Repeat After CuriousGPT', end='\n\n')

    repeat('Curious')
    repeat('is')
    repeat('so')
    repeat('handsome')
    repeat('!')

    print(f'Flag : {FLAG}')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
