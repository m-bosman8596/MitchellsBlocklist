import json

file = open('data.json',)
masterFile = open('myBlocklist.txt', 'w')
json = json.load(file)

prepend_string = '0.0.0.0'
for i in json['action_map']:
    print(i)
    if not '192.168' in i:
        masterFile.write(f'{prepend_string} {i}\n')
for i in json['snitch_map']:
    print(i)
    if not '192.168' in i:
        masterFile.write(f'{prepend_string} {i}\n')

file.close()
masterFile.close()
