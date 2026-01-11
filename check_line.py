
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

# Если до и после # есть кавычки то пропускаем
def is_normal_tag(line):
    if '#' in line:
        idx_tag, is_tag = tag_in_line(line)
        if_tag_1 = "'" in line[:idx_tag] and "'" in line[idx_tag+1:]
        if_tag_2 = '"' in line[:idx_tag] and '"' in line[idx_tag+1:]
        if if_tag_1 or if_tag_2:
            return True
    return False
    
        
    
    
    