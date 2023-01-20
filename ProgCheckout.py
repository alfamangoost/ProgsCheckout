import re

prg_name = '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s08'
line_index = []
# with open("test_log.txt", 'r') as log_file:
with open("EDIT_LOG.txt", 'r') as log_file:
    log = log_file.readlines()
    for line in log:
        # print(line)
        if re.search(prg_name, line) != None:
            #print(line)
            index_of_block_time = log.index(line) - 7
            block_time = log[index_of_block_time]
            print(block_time)
            print(prg_name[51:53])
            print(block_time[16:20])
            print(block_time[74:81])
            if prg_name[51:53] == "08" and block_time[16:20] == "8:00" and block_time[74:81] == "Новости":
                print("Программа стоит в правильном блоке")
            else:
                print("Программа стоит в неправильном временном блоке или в блоке предназначенном для другой программы")
            line_index.append(log.index(line))


# print(log)
print(line_index)

