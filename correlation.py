# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot

study = numpy.array([6,5,9,9,6,7])
sports = numpy.array([5,5,7,8,4,7])

# 散布図を描く
matplotlib.pyplot.scatter(study, sports)
matplotlib.pyplot.axvline(numpy.mean(study), c="r")
matplotlib.pyplot.axhline(numpy.mean(sports), c="r")

matplotlib.pyplot.grid()
matplotlib.pyplot.xlim(0,10)
matplotlib.pyplot.ylim(0,10)
matplotlib.pyplot.xlabel("study")
matplotlib.pyplot.ylabel("sports")

matplotlib.pyplot.show()

# 相関係数を計算する
diffstudy = study - numpy.mean(study)
diffsports = sports - numpy.mean(sports)

numerator = sum(diffstudy * diffsports)
denominator = numpy.sqrt(sum(diffstudy ** 2)) * numpy.sqrt(sum(diffsports ** 2))

print "correlation:", numerator / denominator
print "correlation coefficient", numpy.corrcoef(study, sports)[0,1]