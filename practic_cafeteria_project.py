class Reservation:
    def __init__(self):
        self.tables_list = []
        self.table = {}
        self.name = ''
        self.assign_table = ''

    def table_list(self, number):  # add tables to the list
        for num in range(number):
            self.table = {f'Table{num+1}': 'available', 'Quest': ''}
            self.tables_list.append(self.table)
        return print(f'Table list: {self.tables_list}')

    def check_reservation(self):
        self.name = input('Please enter your name for reservation check: ')
        # print(f'{self.name}: {self.tables_list}')
        print(self.name)
        for self.table in self.tables_list:
            # print(self.table)
            table_key = list(self.table.keys())
            table_value = list(self.table.values())
            if self.table.get('Quest') == self.name:
                return print(f'{table_key[0]} {table_value} for {self.name}')
            elif self.table.get('Quest') == '':
                print(f"{table_key[0]} is {table_value[0]}")

    def add_reservation(self):
        self.assign_table = input(f'What table would you like, {self.name}?: ')
        for self.table in self.tables_list:
            table_key = list(self.table.keys())
            table_value = list(self.table.values())
            if table_key[0] == self.assign_table:
                self.table[table_key[0]] = "reserved"
                self.table["Quest"] = self.name
                return print(self.tables_list)
        print(f"{self.assign_table} is not in available tables list")
        a = input(f"Enter yes (for continue) or no (for exit): ")
        if a == 'yes':
            self.add_reservation2()

    def add_reservation2(self):
        self.add_reservation()


reservation1 = Reservation()
reservation1.table_list(3)
print(reservation1.check_reservation())
reservation1.add_reservation()
reservation2 = Reservation()
print(reservation2.check_reservation())
reservation2.add_reservation()

