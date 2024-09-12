import csv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#### Function(s) {My work, not stolen}

def getCommaIndices(string: str) -> list:
    # Returns a list with index #s of each comma found in the string
    index_list = []
    for i in range(0,len(string)):
        if string[i] == ',':
            index_list.append(i)
    return index_list

#### Main

#print('Please select the CR1000 log file.')
#Tk().withdraw()
#CRfilepath = askopenfilename()
#os.path.basename(CRfilepath)

#f = open(os.path.basename(CRfilepath), 'r')
f = open('test_table_for_python_script.dat', 'r')
tempread = 0
while tempread < 4:
    f.readline()
    tempread += 1

ML = f.readlines()
f.close()

MLEXTRACT = []
for i in ML:
    MLEXTRACT.append(i[1:20])


g = open('test_fans_speed.txt', 'r')
FL = g.readlines()
g.close()

FLEXTRACT = []
for i in FL:
    FLEXTRACT.append(i[0:19])

KEYINDICES = []
for i in FLEXTRACT:
    for j in range(0,len(MLEXTRACT)):
        if i == MLEXTRACT[j]:
            KEYINDICES.append(j)
            
#### File writing
            
#filename = input('Name the output file (Ex: Test123.csv) \n')
filename = 'Test123.csv'
if os.path.isfile(os.getcwd()):
    os.remove(filename)
    

instance_num = 1
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Date Time', 'SHF1_Average', 'SHF2_Average', 'SHF3_Average', 'Instance#'])
    for i in KEYINDICES:
        post_30 = i+30
        for j in range(0,20):       
            SHF1 = ML[post_30 + j][(((getCommaIndices(ML[post_30 + j]))[1])+1):(getCommaIndices(ML[post_30 + j])[2])]
            SHF2 = ML[post_30 + j][(((getCommaIndices(ML[post_30 + j]))[2])+1):(getCommaIndices(ML[post_30 + j])[3])]
            SHF3 = ML[post_30 + j][(((getCommaIndices(ML[post_30 + j]))[3])+1):(getCommaIndices(ML[post_30 + j])[4])]
            csvwriter.writerow([MLEXTRACT[post_30 + j], SHF1, SHF2, SHF3, str(instance_num)])
        instance_num += 1
q = open('Test123.csv', 'r')
print(q.read())
q.close()

'''
Plan for next steps: Design the final version program with Romina. Cannot index forward/backwards on ML due to differing number of
character spaces/decimals. Must index via commas, create a function/loop that identifies the index range for each needed value and then
assigns those values to a list with the index number from ML. Could be dictionary too.
'''
