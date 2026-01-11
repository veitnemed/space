
# Если первый символ # - строка комменатрий
def line_is_comment(line):
    row = line.strip()
    if row[0] == '#':
        return True
    return False

# Проверка есть ли cимвол # в строке и строка не является комментом
def tag_in_line(line):
    line = line.strip()
    if '#' in line and not line_is_comment(line):
        idx_tag = line.index('#')
        return (idx_tag,True) # Передаем сразу проверку и индекс
    return (None, False)

def is_emty_line(line):
    if line == '':
        return True
    return False

def is_def(line):
    if line.strip()[0:3] == 'def':
    
        return True
    return False
    
        
    
    
    