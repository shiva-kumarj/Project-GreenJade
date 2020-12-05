# Generate predictions on new playlist
import pickle
import numpy as np
import pandas as pd
from category_encoders import CatBoostEncoder
from sklearn import metrics, preprocessing

if __name__ == '__main__':
    df = pd.read_csv('dataset/daily_mix_6.csv')
    test = df.copy()
    #test.drop('Unnamed: 0', axis = 1, inplace = True)
    test.drop(['track_name', 'track_id'], axis = 1, inplace = True)

    cbe = pickle.load(open('saved_models/catboostencoder.pkl', 'rb'))
    X_test = cbe.transform(test)

    # Feature Scaling
    scaler = preprocessing.MinMaxScaler().fit(X_test)
    X_test = scaler.transform(X_test)

    # Load model pickle file
    rf_model = pickle.load(open('saved_models/rf.pkl', 'rb'))

    # Predict
    predict = rf_model.predict(X_test)

    df['prediction'] = predict

    # dump final CSV
    df.to_csv('dm_6_prediction.csv', index = False)

    print(df.head())

