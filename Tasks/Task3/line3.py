
with open('text.txt', encoding='utf-8') as f:
    text = f.read()


while True:
     max_lenght = int(input("enter line lenght "))
     if max_lenght < 15:
         print("line lenght can't be so small")
     else:
         break


def is_line_break(text, break_idx):
    if break_idx + 1 >= len(text):
        return True
    last_char = text[break_idx]
    next_char = text[break_idx+1]
    return not (last_char.isalpha() and next_char.isalpha())


def split_to_rude(text):
    rude_lines = []
    done = 0

    while True:
        if done >= 2:
            break

        if is_line_break(text, max_lenght-1):
            break_idx = max_lenght
        else:
            break_idx = text[:max_lenght].rfind(' ')
        rude_line = text[:break_idx]
        rude_lines.append(rude_line)
        text = text[break_idx:]
        
        if len(text) <= max_lenght:
            done += 1
    
    return rude_lines


def width_line(line, max_lenght):
    number_spaces = max_lenght - len(line)
    if line.count(' ') == 0:
        new_spaces_each = 0
        additional_spaces = 0
    else:
        new_spaces_each = 1 + number_spaces // line.count(' ')
        additional_spaces = number_spaces % line.count(' ')
    
    splitted_line = line.split(' ')
    for i in range(additional_spaces):
        splitted_line[i] += ' '

    return (' ' * new_spaces_each).join(splitted_line)

last_list = []
paragraphs = text.split('\n')
for paragraph in paragraphs:
    rude_lines = split_to_rude(paragraph)
    for rude_line in rude_lines:
        result_line = width_line(rude_line, max_lenght)
        last_list.append(result_line)

abz = '\n'
result = abz.join(last_list)
with open('result_file.txt', "w", encoding='utf-8') as f:
    f.write(result)
        
        
        

print('''
                            ### 
#####   ####  #    # ###### ### 
#    # #    # ##   # #      ### 
#    # #    # # #  # #####   #  
#    # #    # #  # # #          
#    # #    # #   ## #      ### 
#####   ####  #    # ###### ### 
                                ''')


input('\n tape "Enter" to exit ')