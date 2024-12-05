#! -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import pickle
import os
list = ['pig']

tmp = 'D:\\bishe\\faster-rcnn\\faster-rcnn-tensorflow-python3-master\\default\\voc_2007_trainval\default\pig_pr.pkl'
fp = open(tmp,'rb')
a = pickle.load(fp)
plt.ylim([0.0, 1.1])
plt.xlim([0.0, 1.1])
tmp = 'Faster R-CNN Precision-Recall Curve pig'
plt.plot(a['rec'],a['prec'])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(tmp)
plt.show() 