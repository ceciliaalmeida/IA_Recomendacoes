import numpy
import pandas as pd
from keras.models import Sequential
from keras.models import Dense
from keras.models import load_model

# Extrai Respostas dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [sensor1, sensor2, sensor3, movimento] (matrix)
# Return 'ans_data' -> Classificações : [movimento] (matrix)
def extract_answers(all_data):
  ans_data = data_set[:, :3].astype('str')
  return ans_data


# Extrai Valores dos Sensores dos dados de Treinamento
# Param 'all_data'  -> Dados Coletados : [sensor1, sensor2, sensor3, movimento] (matrix)
# Return 'sensor_data' -> Dados dos Sensores : [sensor1, sensor2, sensor3] (matrix)
def extract_sensor_data(all_data):
  sensor_data = data_set[:, 0:2].astype('float')
  return sensor_data


# Normaliza dados do sensor entre valores de 0 a 1
# Param 'sensor_data'  -> Dados Coletados : [sensor1, sensor2, sensor3] (matrix)
# Return 'sensor_data' -> Valores Normalizados
def normalize_data(sensor_data):
  return sensor_data

data_frame = pd.read_csv('dados_coletados.csv')
data_set = df.values()
sensor_data = extract_sensor_data(data_set)
ans_data = extract_answers(data_set)

sensor_data = normalize_data(sensor_data)

# Crição do Modelo 3-3-1
model = Sequential()
model.add(Dense(3, input_dim=3))
model.add(Dense(3))
model.add(Dense(1))

# Compilação do Modelo
model.compile(optimizer='sgd', loss='mse', metrics=['acc'])

# Treinamento do Modelo
x = np.asmatrix(sensor_data)
y = np.asmaxtrix(ans_data)
model.fit(x, y, epochs=3000)

#Salvando Modelo Treinado
model.save('modelo.h5')
