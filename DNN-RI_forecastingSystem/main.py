from unittest import result
from DNN_RI_pred_module import DNN_RI_pred
import numpy as np
import pandas as pd
print('\n===================================================================================')
print('                              DNN-RI Forecast System                               ')
print('===================================================================================')
location= input('\nStep 1: Please choose one location(Taipei, Taichung, Alishan): ')
if location=='Taipei' or location=='Alishan':
    print('\nStep 2: Please fill in the value of 10 atmospheric parameters sequentially.')

    factor_1=input('(1) PS01[ 測站氣壓(hPa) ]: ')
    factor_2=input('(2) PS02[ 海平面氣壓(hPa) ]: ')
    factor_3=input('(3) TX01[ 氣溫(˙C) ]: ')
    factor_4=input('(4) TX05[ 露點溫度(˙C) ]: ')
    factor_5=input('(5) RH01[ 相對濕度(%) ]: ')
    factor_6=input('(6) RH02[ 水氣壓(hPa) ]: ')
    factor_7=input('(7) WD01[ 平均風風速(m/s) ]: ')
    factor_8=input('(8) WD02[ 平均風風向(360˚) ]: ')
    factor_9=input('(9) PP01[ 降水量(mm) ]: ')
    factor_10=input('(10) PP02[ 降水時數(hr) ]: ')

    atmos_factor_list=[factor_1, factor_2, factor_3, factor_4, factor_5, factor_6, 
    factor_7, factor_8, factor_9, factor_10]
    
elif location=='Taichung':
    print('\nStep 2: Please fill in the value of 9 atmospheric parameters sequentially.\n')

    factor_1=input('(1) PS01[ 測站氣壓(hPa) ]: ')
    factor_2=input('(2) TX01[ 氣溫(˙C) ]: ')
    factor_3=input('(3) TX05[ 露點溫度(˙C) ]: ')
    factor_4=input('(4) RH01[ 相對濕度(%) ]: ')
    factor_5=input('(5) RH02[ 水氣壓(hPa) ]: ')
    factor_6=input('(6) WD01[ 平均風風速(m/s) ]: ')
    factor_7=input('(7) WD02[ 平均風風向(360˚) ]: ')
    factor_8=input('(8) PP01[ 降水量(mm) ]: ')
    factor_9=input('(9) PP02[ 降水時數(hr) ]: ')

    atmos_factor_list=[factor_1, factor_2, factor_3, factor_4, factor_5, factor_6, 
    factor_7, factor_8, factor_9]

Pred_result = np.array(DNN_RI_pred(location, atmos_factor_list))

print('=============================================================================\n')
list_header = ['RI value', 'Probability of RI', 'Risk level']
added_header_Pred_result = [list_header, Pred_result]
RI_forecastResult=np.array(added_header_Pred_result)


np.savetxt('./output/'+location+'/'+location+'_RI_forecastResult.csv', RI_forecastResult, delimiter=',',fmt='%s')

df = np.array(pd.read_csv('./output/'+location+'/'+location+'_RI_forecastResult.csv', delimiter=',', header=0))

print('【Forecasted results】\n')
print('(1) RI value = ', df[0,0])
print('(2) Probability of RI = ' + str(df[0,1]) + ' %')
print('(3) Risk level = ', df[0,2])
print('\n=> RI forecast result has been saved as .csv file. Please check out the file \n   in the ''output'' folder\n')

print('=============================================================================\n')

