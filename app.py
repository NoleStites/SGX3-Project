from flask import Flask, jsonify, request
import pandas as pd
import os
import io

# Define your global DataFrame
traffic_df = None

app = Flask(__name__)

def load_traffic_data():
    global traffic_df
    #print("Loading Austin Traffic Data...")
    traffic_df = pd.read_csv("atxtraffic.csv")
    #print(f"Loaded {len(traffic_df)} rows into memory.")

@app.route("/")
def index():
    global traffic_df
    sample = traffic_df.head(10).to_dict(orient="records")
    return jsonify(sample)

@app.route("/head")
def top():
    global traffic_df
    count = int(request.args.get('count'))
    sample = traffic_df.head(count).to_dict(orient="records")
    return jsonify(sample)

# Returns the number of rows and columns in data
@app.route("/shape")
def shape():
    global traffic_df
    shape = traffic_df.shape
    sample = {'rows':shape[0], 'columns':shape[1]}
    return jsonify(sample)

# Returns the columns names
@app.route("/columns")
def columns():
    global traffic_df
    sample = traffic_df.columns.to_list()
    return jsonify(sample)

# Returns the unique values of a given column
@app.route("/UniqueValues")
def unique():
    global traffic_df
    column_name = request.args.get('column')
    sample = traffic_df[column_name].unique().tolist()
    return jsonify(sample)

if __name__ == "__main__":
    load_traffic_data()
    app.run(debug=True, host="0.0.0.0", port=8072)
