# -*- coding: utf-8 -*-
"""tekkeköy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DhxfskPkxtjbYazRFqL8trnmPIUIthxD
"""

from google.colab import files
uploaded = files.upload()

!pip install pyyaml h5py

import io
import pandas as pd
import numpy as np
data = pd.read_excel(io.BytesIO(uploaded['denemetekkeköy.xlsx']))

import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

data = data.fillna(data.mean())   #eksik verileri yok eder

data

plt.figure(figsize=(20,8))
plt.plot(data.Tarih,data.atıkkatı)
plt.show()

data = data.filter(['atıkkatı'])
dataset = data.values
training_data_len = math.ceil( len(dataset) *.8)

scaler = MinMaxScaler(feature_range=(0, 1)) 
scaled_data = scaler.fit_transform(dataset)

train_data = scaled_data[0:training_data_len  , : ]
x_train=[]
y_train = []
for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])

len(train_data)

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))

#LSTM AĞ MODELİ 
model = Sequential()   
model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error',metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=1, epochs=125)         #modeli eğit

test_data = scaled_data[training_data_len - 60: , : ]    #test veri kümesi
#x ve y test veri kümeleri  oluştur
x_test = []    
y_test =  dataset[training_data_len : , : ] 
for i in range(60,len(test_data)):
  x_test.append(test_data[i-60:i,0])

x_test = np.array(x_test)  #x sayısal değere dönüştürür
x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))   # Verileri LSTM tarafından kabul edilen şekle dönüştürün

predictions = model.predict(x_test)    #tahmin işlemleri
predictions = scaler.inverse_transform(predictions)

#rms değerini hesapla
rmse=np.sqrt(np.mean(((predictions- y_test)**2)))
rmse

train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
plt.figure(figsize=(20,8))
plt.title('Model',fontsize=20)
plt.xlabel('Tarih', fontsize=20)
plt.ylabel('atıkkatı', fontsize=20)
plt.plot(train['atıkkatı'])
plt.plot(valid[['atıkkatı', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

valid