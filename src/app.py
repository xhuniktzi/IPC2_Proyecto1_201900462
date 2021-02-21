from models import ListaEnlazada

'''
    TODO:
    - fixear funciones 'delete' cuando se borra sobre una lista vacío
    - fixear funcion 'print' cuando se imprime sobre vacío
'''

if __name__ == '__main__':
    lista = ListaEnlazada()
    lista.add_to_end('1')
    lista.add_to_end('2')
    lista.add_to_end('3')
    lista.add_to_end('4')
    lista.add_to_end('5')
    lista.print_list()
