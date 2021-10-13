
'''
Functia verifica daca un numar este patrat perfect
'''
def is_perfect_square(n):
    if n == 1 or n == 0:
        return True
    h = n // 2
    for i in range(2, h + 1):
        if i * i == n:
            return True
    return False

def test_is_perfect_square():
    assert is_perfect_square(4) == True
    assert is_perfect_square(69) == False
    assert is_perfect_square(121) == True
    assert is_perfect_square(25) == True
    assert is_perfect_square(2) == False
    assert is_perfect_square(40) == False
    assert is_perfect_square(64) == True
    assert is_perfect_square(144) == True
    assert is_perfect_square(100) == True
    assert is_perfect_square(81) == True

'''
Functia cauta cea mai lunga subsecventa de patrate perfecte
rezultatul functiei este construit in lista lst1
'''
def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    lst1 = []
    aux = []
    max = 0
    nr = 0
    for i in lst:
        if is_perfect_square(i) == True:
            nr = nr + 1
            aux.append(i)
        else:
            if nr > max:
                lst1 = aux
                max = nr
            nr = 0
            aux = []
    if nr > max:
        lst1 = aux
    return lst1

def test_get_longest_all_perfect_squares():
    lst = [1, 5, 8, 4, 8, 5, 8, 5, 3, 6, 16, 43, 87, 25, 9, 16, 7, 8, 9, 25]
    assert get_longest_all_perfect_squares(lst) == [25, 9, 16]
    lst = [1, 2, 16, 169, 121]
    assert get_longest_all_perfect_squares(lst) == [16, 169, 121]
    lst = [1, 2, 9, 16, 5, 121, 4, 9]
    assert get_longest_all_perfect_squares(lst) == [121, 4, 9]

'''
Functia scrie un numar din baza 10 in baza 2 si rezultatul este memorat intr-o lista. apoi sunt numarate cifrele de 1
'''
def get_number_of_1_bits_in_binary_nr(n):
    n1 = n
    b = 0
    aux = []
    nr = 0
    while n1 > 0:
        aux.append(n1 % 2)
        n1 = n1 // 2
    for i in aux:
        if i == 1:
            nr = nr + 1
    return nr


'''
Functia cauta cea mai lunga subsecventa de numere care au acelasi numar de biti in reprezentarea lor binara
'''
def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    lst1 = []
    aux = [lst[0]]
    max = 1
    nr = 1
    bit_nr = get_number_of_1_bits_in_binary_nr(lst[0])
    for i in range(1, len(lst)):
        if get_number_of_1_bits_in_binary_nr(lst[i]) == bit_nr:
            nr = nr + 1
            aux.append(lst[i])
        else:
            if nr > max:
                lst1 = aux
                max = nr
            nr = 1
            aux = [lst[i]]
            bit_nr = get_number_of_1_bits_in_binary_nr(lst[i])
    if nr > max:
        lst1 = aux
    return lst1

def get_div_count(n):
    '''
    functia calculeaza numarul de divizori al unui numar.
    :param n:
    :return:
    '''
    nr = 0;
    for i in range(1, n + 1):
        if n % i == 0:
            nr = nr + 1
    return nr

def test_get_div_count():
    assert get_div_count(6) == 4
    assert get_div_count(2) == 2
    assert get_div_count(12) == 6
    assert get_div_count(16) == 5

def get_longest_same_div_count(lst: list[int]) -> list[int]:
    lst1 = []
    aux = [lst[0]]
    max = 1
    nr = 1
    div_nr = get_div_count(lst[0])
    for i in range(1, len(lst)):
        if get_div_count(lst[i]) == div_nr:
            nr = nr + 1
            aux.append(lst[i])
        else:
            if nr > max:
                max = nr
                lst1 = aux
            aux = [lst[i]]
            nr = 1
            div_nr = get_div_count(lst[i])
    if nr > max:
        lst1 = aux
    return lst1

def main():
    while True:
        print('1. Citire date. ')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea 1.')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea 2.')
        print('4. Determinare cea mai lunga subsecventa cu proprietatea 3.')
        print('x. Iesire.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            n = int(input('Numarul de elemente: '))
            lst = []
            print('Introduceti numerele: ')
            for i in range(0, n):
                elem = int(input())
                lst.append(elem)
            print(lst)
        elif optiune == '2':
            if get_longest_all_perfect_squares(lst) == []:
                print('Nu exista astfel de secvente.')
            else:
                print(f'Cea mai lunga subsecventa cu propietatea 1 este {get_longest_all_perfect_squares(lst)}')
        elif optiune == '3':
            print(f'Cea mai lunga subsecventa cu propietatea 2 este {get_longest_same_bit_counts(lst)} ')
        elif optiune == '4':
            print(f'Cea mai lunga subsecventa cu proprietatea 3 este {get_longest_same_div_count(lst)}')
        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')





test_is_perfect_square()
test_get_longest_all_perfect_squares()
test_get_div_count()
main()

