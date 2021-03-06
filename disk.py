def open_file(filename):
    ''' str -> [str]
    Opens file of filename. Returns a list of the line data,
    after the first line.'''

    with open(filename, 'r') as file:
        file.readline()
        file_str_list = file.readlines()
    return file_str_list


def file_list_split(file_str_list):
    file_list = []
    for string in file_str_list:
        new_str = string.strip('\n')
        file_list.append(new_str)
    return file_list


def make_inventory_list(file_list):
    inventory = []
    for string in file_list:
        str_list = string.split(',')
        name = str_list[0]
        rent_rate = int(str_list[1])
        replace_value = int(str_list[2])
        stock = int(str_list[3])
        inventory.append([name, rent_rate, replace_value, stock])
    return inventory


def write_inventory(filename, string):
    with open(filename, 'w') as file:
        file.write(string)


def open_history(filename):
    with open(filename) as file:
        contents = file.read()
    return contents


def open_revenue(filename):
    with open(filename) as file:
        revenue_list = file.readlines()
    return revenue_list


def write_revenue(filename, string):
    with open(filename, 'w') as file:
        file.write(string)


def write_history(filename, string):
    with open(filename, 'a') as file:
        file.write(string)


def disk_main():
    file_name = 'inventory.txt'
    file_str_list = open_file(file_name)
    file_list = file_list_split(file_str_list)
    inventory = make_inventory_list(file_list)
    return inventory
