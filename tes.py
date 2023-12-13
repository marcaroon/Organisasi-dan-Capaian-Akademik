import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.model_selection import train_test_split, RandomizedSearchCV# Import train_test_split function
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

import pickle

dataSets = pd.read_excel('Pengaruh Kegiatan Organisasi dengan Capaian Akademik Mahasiswa.xlsx')
dataSets = pd.DataFrame(dataSets)
dataSets.head()

dataSets = dataSets.drop(['No', "Fakultas", "Jurusan", "Semester", "SKS"], axis=1)
dataSets.head()

dataSets['Jabatan_Organisasi'].replace({'-':0, 'Staff':1, 'Kepala Sub Bagian':2, 'Kepala Bagian':3, 'Sekretaris/Bendahara':4, 'Wakil Ketua':5, 'Ketua':6}, inplace=True)
dataSets['Jabatan_Kepanitiaan'].replace({'-':0, 'Staff':1, 'Kepala Sub Bagian':2, 'Kepala Bagian':3, 'Sekretaris/Bendahara':4, 'Wakil Ketua':5, 'Ketua':6}, inplace=True)
dataSets['Kepuasan'].replace({'Sangat Tidak Puas':1, 'Tidak Puas':2, 'Puas':3, 'Sangat Puas':4}, inplace=True)
dataSets['IPK'].replace({'1.00-1.50':0, '1.51-2.00':1, '2.01-2.50':2, '2.51-3.00':3, '3.01-3.50':4, '3.51-4.00':5}, inplace=True)
dataSets['Jenis_Kelamin'].replace({'Laki-Laki':0, 'Perempuan':1}, inplace=True)
dataSets

scaler = MinMaxScaler()
dataSets_scaled = scaler.fit_transform(dataSets)
dataSets_scaled = pd.DataFrame(dataSets_scaled, columns=dataSets.columns)
dataSets_scaled.head()

feature_cols = ['Jumlah_Organisasi', 'Jumlah_Kepanitiaan', 'IPK','Jabatan_Organisasi','Jabatan_Kepanitiaan']
X = dataSets[feature_cols]
y = dataSets['Kepuasan']

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100) # 70% training and 30% test

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

filename = 'modelnew.sav'
y_pred = rf.predict(X_test)

pickle.dump(rf, open(filename, 'wb'))