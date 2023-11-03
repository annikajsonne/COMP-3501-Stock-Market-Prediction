#Importing the Libraries
import pandas as pd
import NumPy as np
#matplotlib inline
import matplotlib. pyplot as plt
import matplotlib
from sklearn. Preprocessing import MinMaxScaler
from Keras. layers import LSTM, Dense, Dropout
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib. dates as mandates
from sklearn. Preprocessing import MinMaxScaler
from sklearn import linear_model
from Keras. Models import Sequential
from Keras. Layers import Dense
import Keras. Backend as Ks
from Keras. Callbacks import EarlyStopping
from Keras. Optimisers import Adam
from Keras. Models import load_model
from Keras. Layers import LSTM
from Keras. utils.vis_utils import plot_model

#Get the Dataset
df=pd.read_csv('MSFT.csv',na_values=['null'],index_col='Date',parse_dates=True,infer_datetime_format=True)
df.head()

# #Print the shape of Dataframe  and Check for Null Values
# print(“Dataframe Shape: “, df. shape)
# print(“Null Value Present: “, df.IsNull().values.any())
# Output:
# >> Dataframe Shape: (7334, 6)
# >>Null Value Present: False