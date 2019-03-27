import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# Extrai Respostas dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_curso, cod_mat, nota] (matrix)
# Return 'ans_data' -> Classificações : [nota] (matrix)
def extract_answers(all_data):
  ans_data = data_set[:, 2].astype('int')
  return ans_data


# Extrai Valores dos Sensores dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_curso, cod_mat, nota] (matrix)
# Return 'sensor_data' -> Dados do Historico : [cod_curso, cod_mat] (matrix)
def extract_data(all_data):
  subjects_data = data_set[:, 0:2].astype('str')
  return subjects_data


data_frame = pd.read_csv('Perfil_Direito.csv')
data_set = data_frame.get_values()
subjects_data = extract_data(data_set)
ans_data = extract_answers(data_set)

# Crição do Modelo 2-5-1
model = Sequential()
model.add(Dense(2, input_dim=2))
model.add(Dense(5))
model.add(Dense(1))

# Compilação do Modelo
model.compile(optimizer='sgd', loss='mse', metrics=['acc'])

# Treinamento do Modelo
x = subjects_data
y = ans_data
model.fit(x, y, epochs=3000)

#Salvando Modelo Treinado
model.save('modelo.h5')

while 1==1:
  dados = []
  cod_curso = input('Codigo do Curso')
  for i in range(0, 77):
   cod_mat = i
   dados = [cod_curso,str(cod_mat)]
   dados = np.asmatrix(dados)
   nota = model.predict(dados)
   print(nota[0][0])
