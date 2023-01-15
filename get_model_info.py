import pickle
import sqlite3

def get_model_info(model_file):
    # load model from pickle file
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    # get model info
    model_info = {'model_type': str(type(model).__name__),
                  'accuracy': model.score(X_test, y_test)}
    return model_info

def store_in_sqlite(model_info):
    #connect to sqlite database
    conn = sqlite3.connect('model_info.db')
    c = conn.cursor()

    #create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS model_info (model_type text, accuracy real)''')

    # insert model info into table
    c.execute("INSERT INTO model_info VALUES (?,?)",(model_info['model_type'],model_info['accuracy']))

    #commit the transaction
    conn.commit()

    # close connection
    conn.close()

if __name__ == "__main__":
    # get model info
    model_info = get_model_info('traffic_model.pkl')

    # store model info in sqlite db
    store_in_sqlite(model_info)
    print("Model info stored in sqlite database")
