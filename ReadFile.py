import pandas as pd

def readZoo():
    df = pd.read_csv('zoo.csv')
    X_df = df[['hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic','catsize']]
    Y_df = df[['class_type']]

    Xdummies_df = pd.get_dummies(X_df)
    Ydummies_df = Y_df

    X = Xdummies_df.values
    Y = Ydummies_df.values
    return X,Y.ravel()
