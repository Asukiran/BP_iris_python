# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 21:07:39 2018

@author: Horizon
"""

import pandas as pd
import numpy as np
from BP_version3 import BPNeuralNetwork
def dataReader():
   #读取训练数据
   data = pd.read_csv("D:\\workSpace\\TensorFlow\\BP\\ANNeal.csv",header=0)
   return data
   
def dataReader_out():
   #读取训练输出数据
   data_out = pd.read_csv("D:\\workSpace\\TensorFlow\\BP\\ANNeal_output.csv",header=0)
   return data_out

def dataReader_test():
   #读取测试数据
   data_test = pd.read_csv("D:\\workSpace\\TensorFlow\\BP\\ANNeal_test.csv",header=0)
   return data_test

def dataReader_test_out():
   #读取测试输出数据
   data_test_out = pd.read_csv("D:\\workSpace\\TensorFlow\\BP\\ANNeal_test_output.csv",header=0)
   return data_test_out

nn = BPNeuralNetwork([38,5,5],'sigmoid')
data=dataReader()
data_out=dataReader_out()
data_test=dataReader_test()
data_test_out=dataReader_test_out()
'''
当输入参数X为一个样本时增量学习
当输入参数X为多个样本时批量学习
'''               
y=np.array(data_out)
y_test=np.array(data_test_out)
nn.BPalgorithm(data,y,0.6,110)
print(nn.d)

#测试集
nn.generalize(data_test,y_test)