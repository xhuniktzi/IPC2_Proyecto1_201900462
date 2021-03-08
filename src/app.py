from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
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
    output.clear()
    count = 0
    while data.get_size() > count:
        matrix = data.get_by_index(count)
        output_matrix = Matriz(
            'output - {}'.format(matrix.name), matrix.m, matrix.n)
        y_count = 0
        while matrix.n > y_count:
            x_count = 0
            while matrix.m > x_count:
                value = matrix.get(x_count, y_count)
                if value > 0:
                    output_matrix.insert(x_count, y_count, 1)
                else:
                    output_matrix.insert(x_count, y_count, 0)
                x_count = x_count + 1
            y_count = y_count + 1
        output.add_to_end(output_matrix)
        count = count + 1


def write_file(output: ListaEnlazada):
    def save():
        files = [('XML Files', '*.xml')]
        filename = asksaveasfilename(filetypes=files, defaultextension=files)
        return filename

    count = 0
    print('Selecciona una matriz: ')
    while output.get_size() > count:
        print('{}. {}'.format(count, output.get_by_index(count).name))
        count = count + 1

    matrix_index = int(input('> '))
    matrix = output.get_by_index(matrix_index)

    xml_root = ET.Element(
        'matriz', {'nombre': matrix.name, 'm': str(matrix.m), 'n': str(matrix.n)})

    y_count = 0
    while matrix.n > y_count:
        x_count = 0
        while matrix.m > x_count:
            matrix_element = ET.SubElement(
                xml_root, 'dato', {'x': str(x_count), 'y': str(y_count)})
            matrix_element.text = str(matrix.get(x_count, y_count))
            x_count = x_count + 1
        y_count = y_count + 1

    bin_xml = ET.tostring(xml_root)

    with open(save(), 'wb') as f:
        f.write(bin_xml)


def print_info():
    print('> Xhunik Nikol Miguel Mutzutz')
    print('> 201900462')
    print('> Introducción a la Programación y Computación 2, Sección D')
    print('> Ingenieria en Ciencias y Sistemas')
    print('> 4to Semestre')


def render_graph(data: ListaEnlazada, output: ListaEnlazada):
    count = 0
    print('Selecciona una matriz: ')
    while data.get_size() > count:
        print('{}. {}'.format(count, data.get_by_index(count).name))
        count = count + 1

    matrix_index = int(input('> '))
    output_matrix = output.get_by_index(matrix_index)
    data.get_by_index(matrix_index).render_matrix(output_matrix)


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
            write_file(output)
            continue
        if opt == '4':
            print_info()
            continue
        if opt == '5':
            render_graph(data, output)
            continue
        if opt == '6':
            exit()

        flag = False


if __name__ == '__main__':
    lista_matrices = ListaEnlazada()
    matrices_procesadas = ListaEnlazada()
    main_menu(lista_matrices, matrices_procesadas)
