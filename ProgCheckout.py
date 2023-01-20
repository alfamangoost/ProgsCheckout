import re
import datetime
from datetime import date



line_index = []


def search_and_check(file_to_open, prg_news, prg_dh, prg_time, blc_time, blc_name):

    with open(file_to_open, 'r') as log_file:
        log = log_file.readlines()
        for line in log:
            # print(line)
            if re.search(prg_news, line) != None:
                # print(line)
                index_of_line_block_params = log.index(line) - 7
                line_block_params = log[index_of_line_block_params]
                # print(line_block_params)
                # print(prg_news[51:53])
                # print(line_block_params[16:20])
                # print(line_block_params[74:81])
                # print(line[13:32])
                # print(line[30:32])
                print(f"Программа {line[13:32]} стоит в блоке {line_block_params[74:81]} {line_block_params[15:20]}")

                # if prg_news[51:53] == prg_time and line_block_params[16:20] == blc_time \
                #         and line_block_params[74:81] == blc_name:
                #     print(f"Программа {line[13:32]} стоит в блоке {line_block_params[74:81]} {line_block_params[16:20]}")
                # else:
                #     print(
                #         f"Программа {line[13:32]} стоит в неправильном временном блоке "
                #         "или в блоке предназначенном для другой программы")
                #     line_index.append(log.index(line))
            if re.search(prg_dh, line) != None:
                # print(line)
                index_of_line_block_params = log.index(line) - 7
                line_block_params = log[index_of_line_block_params]
                # в блоке 18.30 строка с параметрами блока на -6, а не на -7 строке от строки с названием программы
                print(f"Программа {line[13:33]} стоит в блоке {line_block_params[74:90]} {line_block_params[15:20]}")

            # else:
            #     print("Программа с таким именем файла не найдена")


today = date.today()
tomorrow = today + datetime.timedelta(days=1)

# file_to_open = "EDIT_LOG.txt"
file_to_open = ("//Ics/rdd_sh/dr_planer/djinroot/PLAYLIST/"+str(today)+"/EDIT_LOG.txt")
prg_news = '\s\S\S\SNEWS\s'
prg_dh = '\s\S\S\SДХ\s'
# prg_news = '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s08'
# prg_news = '[Н]NEWS 02 12 22 08'
prg_time = "08"
blc_time = "8:00"
blc_name = "Новости"
# search_and_check("EDIT_LOG.txt", '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s08', "08", "8:00", "Новости")
search_and_check(file_to_open, prg_news, prg_dh, prg_time, blc_time, blc_name)


print(file_to_open)

