# -* - coding: UTF-8 -* -
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib
import dataset
import numpy
import matplotlib.pyplot as plt

datingDataMat,datingLabels=dataset.file2matrix("/home/lipeng/.keras/datasets/datingTestSet2.txt")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*numpy.array(datingLabels), 15.0*numpy.array(datingLabels))
plt.show()
