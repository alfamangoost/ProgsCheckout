import re

line_index = []

def search_and_check(file_to_open, prg_name, prg_time, blc_time, blc_name):

    with open(file_to_open, 'r') as log_file:
        log = log_file.readlines()
        for line in log:
            # print(line)
            if re.search(prg_name, line) != None:
                # print(line)
                index_of_line_block_params = log.index(line) - 7
                line_block_params = log[index_of_line_block_params]
                # print(line_block_params)
                # print(prg_name[51:53])
                # print(line_block_params[16:20])
                # print(line_block_params[74:81])
                if prg_name[51:53] == prg_time and line_block_params[16:20] == blc_time \
                        and line_block_params[74:81] == blc_name:
                    print("Программа стоит в правильном блоке")
                else:
                    print(
                        "Программа стоит в неправильном временном блоке или в блоке предназначенном для другой программы")
                line_index.append(log.index(line))

search_and_check("EDIT_LOG.txt", '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s08', "08", "8:00", "Новости")


