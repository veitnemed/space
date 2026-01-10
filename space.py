file_name = 'code.txt'
file_name_out = 'new_code.txt'

with open(file_name, 'r', encoding = 'utf-8') as file, open(file_name_out, 'w',encoding='utf-8') as note:
    for line in file:
        
        if '#' in line.strip():
            if line.strip()[0] == '#':
                continue
            else:
                idx = line.index('#')
                if line[idx+1] =="'" and line[idx-1] =="'":
                    continue 
                else:
                    line_out = line[:idx]
        else:
            if line.strip() != '':
                line_out = line
                note.write(line_out)