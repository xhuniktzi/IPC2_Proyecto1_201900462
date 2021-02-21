from models import ListaEnlazada

if __name__ == '__main__':
    lista_1 = ListaEnlazada()
    lista_1.add_to_end('1')
    lista_1.add_to_end('2')
    lista_1.add_to_end('3')
    lista_1.add_to_end('4')
    lista_1.add_to_end('5')
    lista_1.add_to_end('6')
    lista_1.print_list()
    lista_1.delete_by_index(2)
    lista_1.print_list()
