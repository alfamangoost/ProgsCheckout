import re

line_index = []

def search_and_check(file_to_open, prg_name, prg_time, blc_time):

    with open(file_to_open, 'r') as log_file:
        log = log_file.readlines()
        for line in log:
            # print(line)
            if re.search(prg_name, line) != None:
                # print(line)
                index_of_block_time = log.index(line) - 7
                block_time = log[index_of_block_time]
                print(block_time)
                print(prg_name[51:53])
                print(block_time[16:20])
                print(block_time[74:81])
                if prg_name[51:53] == prg_time and block_time[16:20] == blc_time and block_time[74:81] == "Новости":
                    print("Программа стоит в правильном блоке")
                else:
                    print(
                        "Программа стоит в неправильном временном блоке или в блоке предназначенном для другой программы")
                line_index.append(log.index(line))

search_and_check("EDIT_LOG.txt", '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s08', "08", "8:00" )


