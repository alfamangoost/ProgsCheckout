import re

news = '\s\s\S\S\S\sName\s=\s\S\S\SNEWS\s\d\d\s\d\d\s\d\d\s\d\d'
line_index = []
# with open("test_log.txt", 'r') as log_file:
with open("EDIT_LOG.txt", 'r') as log_file:
    log = log_file.readlines()
    for line in log:
        # print(line)
        if re.search(news, line) != None:
            line_index.append(log.index(line))

# print(log)
print(line_index)

