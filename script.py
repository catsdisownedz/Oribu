import os

path = 'archive/'

dict = {
        'centerlight' : '00',
        'glasses' : '01',
        'happy' : '02',
        'leftlight' : '03',
        'noglasses' :'04',
        'normal' : '05',
        'rightlight' : '06',
        'sad' : '07',
        'sleepy' : '08',
        'surprised' : '09',
        'wink' : '10'
        }

def twoDig(num):
    ret = ""
    if num // 10 == 0:
        ret = "0"
    ret += str(num)
    return ret

for i in range(1, 16):
    os.mkdir(path + twoDig(i))

for file in os.listdir(path):
    if file[0] == '.':
        continue
    os.rename(path + file, path + file[8:10] + "/" + file[0:7] + file[10:])
'''
for file in os.listdir(path):
    if file[0] == '.':
        continue
    print(file)
    new_name = "subject_" + file[7:9] + '_' + dict[file[10:]] + ".jpg"
    my_source = path + file
    my_dest = path + new_name
    os.rename(my_source, my_dest)
'''
