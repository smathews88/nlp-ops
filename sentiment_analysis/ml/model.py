# Creating model architecture.
from sentiment_analysis.entity.config_entity import ModelTrainerConfig
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.optimizers import RMSprop
from keras._tf_keras.keras.callbacks import EarlyStopping, ModelCheckpoint
from keras._tf_keras.keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D
from sentiment_analysis.constants import *

class ModelArchitecture:

    def __init__(self):
        pass

    
    def get_model(self):
        model = Sequential()
        model.add(Embedding(MAX_WORDS, 100,input_length=MAX_LEN))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100,dropout=0.2,recurrent_dropout=0.2))
        model.add(Dense(1,activation=ACTIVATION))
        model.summary()
        model.compile(loss=LOSS,optimizer=RMSprop(),metrics=METRICS)

        return model