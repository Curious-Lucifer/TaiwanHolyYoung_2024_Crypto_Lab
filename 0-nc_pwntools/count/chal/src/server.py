import sys

from secret import FLAG

def main():
    print('Description : Count Number', end='\n\n')

    for i in range(100):
        print(f'Round {i + 1}')
        try:
            inp_num = int(input('> '))
        except ValueError:
            print('Error : not integer')
            sys.exit()
        
        if inp_num != (i + 1):
            print('Error : wrong number')
            sys.exit()

    print(f'Flag : {FLAG}')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()

