from flask import Flask, jsonify, request

# Used to Convert Parsed data into a pandas dataframe
import pandas as pd

# Importing Json
import json

import pymongo

import traceback

# Creating Database connection
myclient = pymongo.MongoClient("localhost", 27017)

# database
db = myclient["test2"]

# Created or Switched to collection
Collection = db["test"]


# http://127.0.0.1:5000/inserting_data?url==https://www.auto-data.net/en/audi-100-avant-4a-c4-2.8-e-174hp-automatic-26292
# creating a Flask app
app = Flask(__name__)


@app.route("/inserting_data")
def inserting_data():

    try:
    
       url = request.args.get('url')
       dfs = pd.read_html(url)

       df = pd.DataFrame(dfs[1])

       records = json.loads(df.T.to_json())

       records2 = flatten_dict(records)
       #print(records2)

       new_dict = []
       for value in records2.values():
            new_dict.append(value)

       final_data_to_insert = Convert(new_dict)
       for key, value in final_data_to_insert.items():
            if value == '(adsbygoogle = window.adsbygoogle || []).push({});':
                final_data_to_insert.pop(key)
                break
       
       Collection.insert_one(final_data_to_insert)
    

       return jsonify("Data Inserted Successfully")
    except Exception as ex:
        print("Exception in generate_json : ",(str(ex)))
        print(traceback.print_exc())
        return jsonify("Exception in generate_json.")


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }
             

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct



# driver function
if __name__ == "__main__":
    app.run(debug=True)
