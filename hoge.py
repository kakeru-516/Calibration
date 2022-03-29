import numpy as np

import numpy as np

txt = np.loadtxt('output2.csv', dtype='unicode', delimiter=',')
error1 = np.zeros(shape=(149, 1))
error2 = np.zeros(shape=(149, 1))
error3 = np.zeros(shape=(149, 1))
error4 = np.zeros(shape=(149, 1))
txt = np.append(txt, error1, axis=1)
txt = np.append(txt, error2, axis=1)
txt = np.append(txt, error3, axis=1)
txt = np.append(txt, error4, axis=1)
txt[0][5] = 'error[%]'
txt[0][6] = 'error2[%]'
txt[0][7] = 'error[m]'
txt[0][8] = 'error2[m]'
j = 0
for i in range(1, 149) :
    if i % 3 != 1 :
        txt[i][0] = (j + 1) * 20
    if i % 3 == 0 :
        j += 1

for i in range(1, 149) :
    txt[i][5] = abs(float(txt[i][0]) - float(txt[i][3])) * 100 / float(txt[i][0])
    txt[i][6] = abs(float(txt[i][0]) - float(txt[i][4])) * 100 / float(txt[i][0])
    txt[i][7] = abs(float(txt[i][0]) - float(txt[i][3]))
    txt[i][8] = abs(float(txt[i][0]) - float(txt[i][4]))

np.set_printoptions(precision=3)
np.savetxt('output3.csv', txt, fmt='%s', delimiter=',')
