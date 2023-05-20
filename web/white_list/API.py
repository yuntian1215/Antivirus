

white_list = ['Dir1', 'Dir2', 'Dir3']


def add_Dir(dir: str):
    white_list.append(dir)
    print('add_Dir:', white_list)

def del_Dir(dir: str):
    white_list.remove(dir)
    print('del_Dir:', white_list)
