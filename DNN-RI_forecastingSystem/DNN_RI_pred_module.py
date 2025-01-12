


import sys
import json
import numpy as np


def DNN_RI_pred(location, input_data):
    
    from math import gamma
    from re import T
    import sys
    from pyexpat import model
    from stringprep import b1_set
    from tkinter import E
    import tensorflow as tf
    from keras.models import Sequential
    from keras.optimizers import Adam, Adagrad
    from keras.layers import Dense, Activation, Dropout
    import pandas as pd  
    import numpy as np

    global pred_6, pred_12, pred_18, pred_24
    input_data = np.array(input_data).astype(float)
    input_data = np.reshape(input_data, (1,-1))
    station_parameter= np.array(pd.read_csv('./station_parameter/'+location+'_parameter.csv', header=None))

    # opt= 'Adagrad', 'Adam'    # Optimizer
    # act= 'sigmoid','tanh'     # Activation
    # bs=[16, 32, 64, 128, 256, 512]    # batch_size => total option
    # lr=[0.1, 0.01, 0.001, 0.0001]  # learning rate => total option
    # nd=[i*5 for i in range(2,21)]   # node = Iterable of number hidden units per layer => total option

    station=['Taichung', 'Taipei', 'Alishan']
    lead_time=['6', '12', '18', '24']
    all_pred_value=np.empty(len(lead_time))
    if location == station[0]:
        for lt in range(1, len(lead_time)+1):
            if lt*6==int(lead_time[0]):
                model = Sequential()
                model.add(Dense(int(station_parameter[0,7]), input_dim=input_data.size, activation=station_parameter[0,4]))
                model.add(Dense(int(station_parameter[0,8]), input_dim=input_data.size, activation=station_parameter[0,4]))
                model.add(Dense(int(station_parameter[0,9]), input_dim=input_data.size, activation=station_parameter[0,4]))
                model.add(Dense(int(station_parameter[0,10]), input_dim=input_data.size, activation=station_parameter[0,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[0,5])), 
                            metrics=['mse'])
                pred_6 = float(model.predict(input_data, batch_size=int(station_parameter[0,6])))
                all_pred_value[0]=pred_6

            elif lt*6==int(lead_time[1]):
                model = Sequential()
                model.add(Dense(int(station_parameter[1,7]), input_dim=input_data.size, activation=station_parameter[1,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[1,5])), 
                            metrics=['mse'])

                pred_12 = float(model.predict(input_data, batch_size=int(station_parameter[1,6])))
                all_pred_value[1]=pred_12

            elif lt*6==int(lead_time[2]):
                model = Sequential()
                model.add(Dense(int(station_parameter[2,7]), input_dim=input_data.size, activation=station_parameter[2,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adagrad(learning_rate=float(station_parameter[2,5])), 
                            metrics=['mse'])

                pred_18 = float(model.predict(input_data, batch_size=int(station_parameter[2,6])))
                all_pred_value[2]=pred_18

            elif lt*6==int(lead_time[3]):
                model = Sequential()
                model.add(Dense(int(station_parameter[3,7]), input_dim=input_data.size, activation=station_parameter[3,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adagrad(learning_rate=float(station_parameter[3,5])), 
                            metrics=['mse'])

                pred_24 = float(model.predict(input_data, batch_size=int(station_parameter[3,6])))
                all_pred_value[3]=pred_24
                
        RI_value= round(sum(all_pred_value)/len(lead_time), 2)


        count=0
        for i in range(len(all_pred_value)):
            if all_pred_value[i]>=30:
                count+=25            
        Prob = int(count)


        if Prob == 0:
            risk_level = 'Safe'

        elif Prob == 25:
            risk_level = 'Low'

        elif Prob == 50:
            risk_level = 'Medium'

        elif Prob == 75:
            risk_level = 'High'

        elif Prob == 100:
            risk_level = 'Quite high'

        lst = [RI_value, Prob, risk_level]

    elif location == station[1]:
        for lt in range(1, len(lead_time)+1):
            if lt*6==int(lead_time[0]):

                model = Sequential()
                model.add(Dense(int(station_parameter[0,7]), input_dim=input_data.size, activation=station_parameter[0,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[0,5])), 
                            metrics=['mse'])
                pred_6 = float(model.predict(input_data, batch_size=int(station_parameter[0,6])))
                all_pred_value[0]=pred_6
                
            elif lt*6==int(lead_time[1]):
                model = Sequential()
                model.add(Dense(int(station_parameter[1,7]), input_dim=input_data.size, activation=station_parameter[1,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[1,5])), 
                            metrics=['mse'])
                pred_12 = float(model.predict(input_data, batch_size=int(station_parameter[1,6])))
                all_pred_value[1]=pred_12

            elif lt*6==int(lead_time[2]):
                model = Sequential()
                model.add(Dense(int(station_parameter[2,7]), input_dim=input_data.size, activation=station_parameter[2,4]))
                model.add(Dense(int(station_parameter[2,8]), input_dim=input_data.size, activation=station_parameter[2,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[2,5])), 
                            metrics=['mse'])
                pred_18 = float(model.predict(input_data, batch_size=int(station_parameter[2,6])))
                all_pred_value[2]=pred_18

            elif lt*6==int(lead_time[3]):
                model = Sequential()
                model.add(Dense(int(station_parameter[3,7]), input_dim=input_data.size, activation=station_parameter[3,4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adagrad(learning_rate=float(station_parameter[3,5])), 
                            metrics=['mse'])
                pred_24 = float(model.predict(input_data, batch_size=int(station_parameter[3,6])))
                all_pred_value[3]=pred_24

        RI_value= round(sum(all_pred_value)/len(lead_time), 2)


        count=0
        for i in range(len(all_pred_value)):
            if all_pred_value[i]>=30:
                count+=25            
        Prob = int(count)


        if Prob == 0:
            risk_level = 'Safe'

        elif Prob == 25:
            risk_level = 'Low'

        elif Prob == 50:
            risk_level = 'Medium'

        elif Prob == 75:
            risk_level = 'High'

        elif Prob == 100:
            risk_level = 'quite'

        lst = [RI_value, Prob, risk_level]

    elif location == station[2]:
        for lt in range(1, len(lead_time)+1):
            if lt*6==int(lead_time[0]):
                model = Sequential()
                model.add(Dense(int(station_parameter[0,7]), input_dim=input_data.size, activation=station_parameter[0][4]))
                model.add(Dense(int(station_parameter[0,8]), input_dim=input_data.size, activation=station_parameter[0][4]))
                model.add(Dense(int(station_parameter[0,9]), input_dim=input_data.size, activation=station_parameter[0][4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[0,5])), 
                            metrics=['mse'])
                pred_6 = model.predict(input_data)
                all_pred_value[0]=pred_6

            elif lt*6==int(lead_time[1]):
                model = Sequential()
                model.add(Dense(int(station_parameter[1,7]), input_dim=input_data.size, activation=station_parameter[1][4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adam(learning_rate=float(station_parameter[1,5])), 
                            metrics=['mse'])
                pred_12 = model.predict(input_data)
                all_pred_value[1]=pred_12

            elif lt*6==int(lead_time[2]):
                model = Sequential()
                model.add(Dense(int(station_parameter[2,7]), input_dim=input_data.size, activation=station_parameter[2][4]))
                model.add(Dense(int(station_parameter[2,8]), input_dim=input_data.size, activation=station_parameter[2][4]))
                model.add(Dense(int(station_parameter[2,9]), input_dim=input_data.size, activation=station_parameter[2][4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adagrad(learning_rate=float(station_parameter[2,5])), 
                            metrics=['mse'])
                pred_18 = model.predict(input_data)
                all_pred_value[2]=pred_18

            elif lt*6==int(lead_time[3]):
                model = Sequential()
                model.add(Dense(int(station_parameter[3,7]), input_dim=input_data.size, activation=station_parameter[3][4]))
                model.add(Dense(int(station_parameter[3,8]), input_dim=input_data.size, activation=station_parameter[3][4]))
                model.add(Dropout(0.5))
                model.add(Dense(1))
                model.compile(loss= 'mse',
                            optimizer=Adagrad(learning_rate=float(station_parameter[3,5])), 
                            metrics=['mse'])
                pred_24 = model.predict(input_data)
                all_pred_value[3]=pred_24

        RI_value= round(sum(all_pred_value)/len(lead_time), 2)

        count=0
        for i in range(len(all_pred_value)):
            if all_pred_value[i]>=30:
                count+=25            
        Prob = int(count)


        if Prob == 0:
            risk_level = 'Safe'

        elif Prob == 25:
            risk_level = 'Low'

        elif Prob == 50:
            risk_level = 'Medium'

        elif Prob == 75:
            risk_level = 'High'

        elif Prob == 100:
            risk_level = 'Quite high'

        lst = [RI_value, Prob, risk_level]

    return lst






location = ["Taipei"]
result = [ sys.argv[1],  sys.argv[2],sys.argv[3] , sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]

Pred_result = np.array(DNN_RI_pred(location, result))







# print(result["Name"])

# result = json.dumps(Pred_result)
print(str(Pred_result))

# print(str(json))
# sys.stdout.flush()
