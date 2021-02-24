from tkinter import Tk
from tkinter.filedialog import askopenfilename
from xml.etree import ElementTree as ET
from models import ListaEnlazada
from models import Matriz


def load_file(data: ListaEnlazada):
    Tk().withdraw()
    filename = askopenfilename()
    xml_tree = ET.parse(filename)
    xml_root = xml_tree.getroot()
    for matrix in xml_root:
        matrix_attrib = matrix.attrib
        data.add_to_end(Matriz(matrix_attrib['nombre'], int(matrix_attrib['m']),
                               int(matrix_attrib['n'])))
        for obj in matrix:
            obj_attrib = obj.attrib
            data.get_last().insert(int(obj_attrib['x'])-1,
                                   int(obj_attrib['y'])-1, int(obj.text))


def process_file(data: ListaEnlazada, output: ListaEnlazada):
    count = 0
    while data.get_size() > count:
        matrix = data.get_by_index(count)
        process_matrix = Matriz(matrix.name, matrix.m, matrix.n)
        redux_matrix = Matriz(matrix.name, matrix.m, matrix.n)

        y_count = 0
        while matrix.n > y_count:
            x_count = 0
            while matrix.m > x_count:
                if matrix.get(x_count, y_count) >= 1:
                    process_matrix.insert(x_count, y_count, 1)
                else:
                    process_matrix.insert(x_count, y_count, 0)
                x_count = x_count + 1
            y_count = y_count + 1
        count = count + 1

        matrix.print_matrix()
        process_matrix.print_matrix()


def main_menu(data: ListaEnlazada, output: ListaEnlazada):
    flag = True
    while flag:
        print('Menu Principal')
        print('---')
        print('1. Cargar archivo')
        print('2. Procesar archivo')
        print('3. Escribir archivo de salida')
        print('4. Mostrar datos del estudiante')
        print('5. Generar gráfica')
        print('6. Salir')
        opt = input('> ')

        if opt == '1':
            load_file(data)
            continue
        if opt == '2':
            process_file(data, output)
            continue
        if opt == '3':
            continue
        if opt == '4':
            continue
        if opt == '5':
            continue
        if opt == '6':
            exit()

        flag = False


if __name__ == '__main__':
    lista_matrices = ListaEnlazada()
    matrices_procesadas = ListaEnlazada()
    main_menu(lista_matrices, matrices_procesadas)
    pass
