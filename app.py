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

# How many "traffic hazard" incidents occurred in 2023? 2024?
@app.route("/ValueCountByYear")
def value_count():
    global traffic_df
    column_name = request.args.get('ColumnName')
    column_value = request.args.get('ColumnValue')
    year = int(request.args.get('Year'))

    if (None in [column_name, column_value, year]):
        return jsonify({"error", "Missing parameter"}), 500
    
    year_df = traffic_df.copy()
    year_df['year'] = pd.to_datetime(year_df['Published Date']).dt.year
    #sample = year_df[(year_df[column_name] == column_value) & (year_df['year'] == year)].to_dict(orient="records")
    sample = year_df[(year_df[column_name] == column_value) & (year_df['year'] == year)].to_json()
    return jsonify(sample)

@app.route("/BetweenTimes")
def between_times():
    global traffic_df
    hour1  = int(request.args.get('hour1'))
    hour2  = int(request.args.get('hour2'))
    
    hour_df = traffic_df.copy()
    hour_df['hour'] = pd.to_datetime(hour_df['Published Date']).dt.hour
    
    sample = hour_df[(hour_df['hour'] >= hour1) & (hour_df['hour'] <= hour2)]
    sample = sample.drop(columns=['hour']).to_dict(orient='records')
    return jsonify(sample)

if __name__ == "__main__":
    load_traffic_data()
    app.run(debug=True, host="0.0.0.0", port=8072)
