from models import ListaEnlazada


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
        size = self.row_list.get_size()
        while size > count:
            self.row_list.get_by_index(count).print_list()
            count = count + 1
        print()