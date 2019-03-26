import numpy
import pandas as pd
from keras.models import Sequential
from keras.models import Dense
from keras.models import load_model

# Extrai Respostas dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_1, cod_2, cod_3, cod_4, cod_5, cod_6] (matrix)
# Return 'ans_data' -> Classificações : [cod_6] (matrix)
def extract_answers(all_data):
  ans_data = data_set[:, :5].astype('int')
  return ans_data


# Extrai Valores dos Sensores dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [cod_1, cod_2, cod_3, cod_4, cod_5, cod_6] (matrix)
# Return 'sensor_data' -> Dados do Historico : [cod_1, cod_2, cod_3, cod_4, cod_5] (matrix)
def extract_data(all_data):
  subjects_data = data_set[:, 0:4].astype('int')
  return subjects_data


data_frame = pd.read_csv('dados_coletados.csv')
data_set = df.values()
subjects_data = extract_data(data_set)
ans_data = extract_answers(data_set)


# Crição do Modelo 5-5-1
model = Sequential()
model.add(Dense(5, input_dim=3))
model.add(Dense(5))
model.add(Dense(1))

# Compilação do Modelo
model.compile(optimizer='sgd', loss='mse', metrics=['acc'])

# Treinamento do Modelo
x = np.asmatrix(sensor_data)
y = np.asmaxtrix(ans_data)
model.fit(x, y, epochs=3000)

#Salvando Modelo Treinado
model.save('modelo.h5')

while true:
  dados = []
  for i in range(0,5):
    i = int(input('Codigo Historico ' + str(i+1) + ' :'))
    dados.append(i)
  dados = np.asmatrix(dados)
  model.predict(dados)
