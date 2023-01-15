import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model(data):
    # split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('label', axis=1), data['label'], test_size=0.2)

    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy)

    return model

if __name__ == "__main__":
    # load traffic data
    data = pd.read_csv("traffic_data.csv")

    # train model
    model = train_model(data)

    # save model
    with open('traffic_model.pkl', 'wb') as f:
        pickle.dump(model, f)
