from pprint import pprint

# d = dict()

# d['a'] = 1
# d['b'] = 5
# d['c'] = 7

# d = {
#     'a': 1,
#     'b': 5,
#     'c': 7
# }

# print(d)
# pprint(d, width=4)
# if 'a' in d:
#     print(d['a'])
# else:
#     print('No existe la llave')
import json

d = {}

while True:
    print('1) Agregar key y value')
    print('2) Sacar un value')
    print('3) Mostrar keys')
    print('4) Mostrar key-value')
    print('5) Eliminar key')
    print('6) Vaciar')
    print('7) Mostrar Valores')
    print('8) Respaldar')
    print('9) Recuperar')
    print('0) Salir')
    op = input('> ')

    if op == '1':
        key = input('Key: ')
        value = int(input('Value: '))

        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
    elif op == '2':
        key = input('Key: ')

        if key in d:
            print(d[key])
        else:
            print(f'{key} no existe')
    elif op == '3':
        for key in d.keys():
            print(key)
    elif op == '4':
        for key, value in d.items():
            print(key, value)
    elif op == '5':
        key = input('Key: ')

        if key in d:
            d.pop(key) # del d[key]
        else:
            print(f'{key} no existe')
    elif op == '6':
        d.clear()
    elif op == '7':
        for value in d.values():
            print(value)
    elif op == '8':
        with open('dict.json', 'w') as file:
            json.dump(d, file, indent=5)
    elif op == '9':
        with open('dict.json', 'r') as file:
            d = json.load(file) 
    elif op == '0':
        break
