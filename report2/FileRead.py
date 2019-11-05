import os
import pandas as pd
import numpy as np

def ReadAge():
    #print(os.sys.path)
    TrainUrl = "../titanic/train.csv"
    TestUrl = "../titanic/test.csv"
    TrainDf = pd.read_csv(TrainUrl)
    TestDf = pd.read_csv(TestUrl)   
    TrainAgeMedian = TrainDf["Age"].fillna(TrainDf["Age"].median())
    TrainAgeMean = TrainDf["Age"].fillna(TrainDf["Age"].mean())

    return TrainAgeMedian ,TrainAgeMean

def ReadSex():
    TrainUrl = "../titanic/train.csv"
    TestUrl = "../titanic/test.csv"
    TrainDf = pd.read_csv(TrainUrl)
    TestDf = pd.read_csv(TestUrl)
    pclass = TrainDf["Pclass"]
    label = TrainDf.loc[:,["Survived"]].values
    p_test = TestDf["Pclass"]
    


if __name__ == "__main__":
    #main()
    hoge = ReadAge()

