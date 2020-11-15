import glob 

trains = []
tests = []

count = 0
for path in glob.glob('wavs_raw/*.wav'):
    if count <= 100:
        tests.append(path.split('/')[-1].split('.')[0])
    else:
        trains.append(path.split('/')[-1].split('.')[0])
    count+=1

f = open('training.txt','a')
g = open('validation.txt','a')

for test in tests:
    g.write(test+"\n")
for train in trains:
    f.write(train+"\n")

f.close()
g.close()
