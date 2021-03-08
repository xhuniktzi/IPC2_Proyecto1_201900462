from models import ListaEnlazada, Matriz
from os import system, startfile


class Matriz:
    def __init__(self, name: str, m: int, n: int):
        self.name = name
        self.m = m
        self.n = n
        self.row_list = ListaEnlazada()

        count_rows = 0
        while self.n > count_rows:
            row = ListaEnlazada()

            count_cols = 0
            while self.m > count_cols:
                row.add_to_end(None)
                count_cols = count_cols + 1

            self.row_list.add_to_end(row)
            count_rows = count_rows + 1

    def insert(self, x: int, y: int, data):
        row = self.row_list.get_by_index(y)
        row.set_by_index(x, data)

    def get(self, x: int, y: int):
        row = self.row_list.get_by_index(y)
        return row.get_by_index(x)

    def print_matrix(self):
        count = 0
        print(self.name)
        size = self.row_list.get_size()
        while size > count:
            self.row_list.get_by_index(count).print_list()
            count = count + 1
        print()

    def render_matrix(self, process: Matriz):
        temp_file = open('graph.dot', 'w+')
        temp_file.write('digraph G {\n')  # begin file
        temp_file.write('name [label="{}"];\n'.format(self.name))
        temp_file.write('m [label="m={}"];\n'.format(self.m))
        temp_file.write('n [label="n={}"];\n'.format(self.n))
        temp_file.write('name -> m;')
        temp_file.write('name -> n;')

        # Gráfica entrada
        x_count = 0
        while self.m > x_count:

            y_count = 0
            while self.n > y_count:
                temp_file.write('x{}y{} [label="{}"];\n'.format(
                    x_count, y_count, self.get(x_count, y_count)))

                if not (y_count + 1) >= self.n:
                    temp_file.write(
                        'x{}y{} -> x{}y{};\n'.format(x_count, y_count, x_count, y_count+1))
                y_count = y_count + 1

            temp_file.write('name -> x{}y{};'.format(x_count, 0))
            x_count = x_count + 1

        # Gráfica salida procesada
        temp_file.write('proc_name [label="{}"];\n'.format(process.name))
        temp_file.write('proc_m [label="m={}"];\n'.format(process.m))
        temp_file.write('proc_n [label="n={}"];\n'.format(process.n))
        temp_file.write('proc_name -> proc_m;')
        temp_file.write('proc_name -> proc_n;')
        p_x_count = 0
        while process.m > p_x_count:
            p_y_count = 0
            while process.n > p_y_count:
                temp_file.write('px{}py{} [label="{}"];\n'.format(
                    p_x_count, p_y_count, process.get(p_x_count, p_y_count)))

                if not (p_y_count + 1) >= process.n:
                    temp_file.write(
                        'px{}py{} -> px{}py{};\n'.format(p_x_count, p_y_count, p_x_count, p_y_count+1))
                p_y_count = p_y_count + 1

            temp_file.write('proc_name -> px{}py{};'.format(p_x_count, 0))
            p_x_count = p_x_count + 1

        temp_file.write('}\n')  # end file
        temp_file.close()
        system('dot -Tsvg graph.dot -o output.svg')
        startfile('output.svg')
