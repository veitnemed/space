def is_not_empty_file(name_file):
    # Проверка не пустой ли файл
    
    with open(name_file,'r',encoding='utf-8') as file:
        text = file.readline()
        if text == []:
            return False
    return True



        
