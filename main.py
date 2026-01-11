import work_file as wf
import is_not_empty_file as ef
from print_message import print_messeage

file_name = 'code.txt'
file_name_output = 'new_code.txt'


if __name__ == '__main__':
    
    print_messeage('start')
    if ef.is_not_empty_file(file_name):
        wf.working_on_code(file_name,file_name_output)
        print_messeage('end')
    else:
        print_messeage('emty')
    
    