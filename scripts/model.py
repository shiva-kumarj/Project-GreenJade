# Train RF model using best params obtained from grid search CV

import pandas as pd
import numpy as np
import pickle
from category_encoders import CatBoostEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

if __name__ == '__main__':
    df = pd.read_csv('dataset/data.csv')
    y = df['target']
    df.drop('target', axis = 1, inplace = True)
    perm = np.random.permutation(len(df))
    train = df.iloc[perm].reset_index(drop = True)
    y = y.iloc[perm].reset_index(drop = True)

    # drop columns
    train.drop(['track_name', 'track_id'], axis = 1, inplace = True)

    # Categorical Encoding
    cbe = CatBoostEncoder(cols = ['artist', 'album'])
    cbe = cbe.fit(train, y)
    pickle.dump(cbe, open('saved_models/catboostencoder.pkl', 'wb'))
    train = cbe.transform(train)

    # Feature Scaling
    scaler = MinMaxScaler().fit(train)
    train = scaler.transform(train)

    # Model
    rf_model = pickle.load(open('saved_models/random_forest_grid_model.pkl', 'rb'))
    new_model = RandomForestClassifier(
        criterion = rf_model.best_params_['criterion'],
        min_impurity_decrease = rf_model.best_params_['min_impurity_decrease'],
        min_samples_leaf = rf_model.best_params_['min_samples_leaf'],
        n_estimators = rf_model.best_params_['n_estimators']
    )

    new_model = new_model.fit(train, y)
    print("data shape: ", train.shape)
    # dump trained model
    pickle.dump(new_model, open('saved_models/rf.pkl', 'wb'))
