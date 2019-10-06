from os import listdir
from os.path import isfile,join
sentences = []

directory_name = "Suits - season 1.en"
files = [f for f in listdir(directory_name) if isfile(join(directory_name,f))]

for file_name in files:
    with open(join(directory_name,file_name)) as f:
        data = f.read()
        l = [x for x in data.split("\n") if not x.isnumeric() and "-->" not in x]
        print(l)
