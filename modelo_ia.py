import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# Extrai Respostas dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_curso, cod_mat, nota] (matrix)
# Return 'ans_data' -> Classificações : [nota] (matrix)
def extract_answers(all_data):
  ans_data = data_set[:, 2].astype('str')
  return ans_data


# Extrai Valores dos Sensores dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_curso, cod_mat, nota] (matrix)
# Return 'sensor_data' -> Dados do Historico : [cod_curso, cod_mat] (matrix)
def extract_data(all_data):
  subjects_data = data_set[:, 0:2].astype('int')
  return subjects_data


data_frame = pd.read_csv('Perfil_Direito.csv')
data_set = data_frame.get_values()
subjects_data = extract_data(data_set)
ans_data = extract_answers(data_set)

encoder = LabelEncoder()
encoded = encoder.fit_transform(ans_data)

# Crição do Modelo
model = Sequential()
model.add(Dense(6, input_dim=2, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.add(Dense(6, activation='softmax'))

# Compilação do Modelo
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['acc'])

# Treinamento do Modelo
x = subjects_data
y = np_utils.to_categorical(encoded)
model.fit(x, y, epochs=10000)

#Salvando Modelo Treinado
model.save('modelo.h5')

while 1==1:
  dados = []
  cod_curso = input('Codigo do Curso')
  for i in range(1, 78):
   cod_mat = i
   dados = [cod_curso,cod_mat]
   dados = np.asmatrix(dados)
   nota = model.predict_classes(dados)
   print('Codigo Materia : ' + str(cod_mat) + ' - Nota : ' + str(nota[0]))
