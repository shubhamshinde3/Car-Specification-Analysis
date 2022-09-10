from flask import Flask, jsonify, request

# Library used for opening and reading
import urllib.request

# Used for parsing all the tables present in the WebSite
#from html_table_parser.parser import HTMLTableParser --commented by prachi


# Used to Convert Parsed data into a pandas dataframe
import pandas as pd


# Importing Json
import json
import csv

# from pymongo import MongoClient
import pymongo

import traceback

# Creating Database connection
myclient = pymongo.MongoClient("localhost", 27017)

# database
db = myclient["Cars_test"]

# Created or Switched to collection
Collection = db["Data_test"]


# http://127.0.0.1:5000/generate_json?url=https://www.auto-data.net/en/audi-100-avant-4a-c4-2.8-e-174hp-automatic-26292
# creating a Flask app
app = Flask(__name__)


@app.route("/generate_json")
def generate_json():

    try:
        url = request.args.get("url")
        # defining the html contents of a URL.
        xhtml = get_data(url).decode("utf-8")
        dfs1 = pd.read_html(xhtml , attrs={"class" : "cardetailsout car2"})
        dfs2 = dfs1[0]
        dfs3 = dfs2.T
        dfs3
        dfs3.rename(columns=dfs3.iloc[0], inplace = True)
        dfs4 = dfs3[1:]
        dfs4 = dfs4.drop(['(adsbygoogle = window.adsbygoogle || []).push({});'], axis = 1)
        dfs4
    
        # Defining the HTMLTableParser object
        #parser = HTMLTableParser() --commented by prachi

        # Storing the returned html data in the HTMLTableParser object.
        #parser.feed(xhtml) --commented by prachi

        # Converting the parsed data to PandasDataFrame.
       # pd.set_option("display.max_rows", len(parser.tables[1]))
       # print("\n\nPANDAS DATAFRAME\n")
       # print(pd.DataFrame(parser.tables[1]))
       # df = pd.DataFrame(parser.tables[1])
       # df.dropna(inplace=True)

        # now = datetime.now()
        # dt_string = now.strftime("%d%m%Y%H%M%S")
      #  df.to_json("temp" ".json", orient="values")

      #  dump_data()

        dfs4.to_csv('file2.csv', header=True, index=False)

        return jsonify("Data Inserted Successfully")
    except Exception as ex:
        print("Exception in generate_json : ",(str(ex)))
        print(traceback.print_exc())
        return jsonify("Exception in generate_json.")


# This functions opens a website and reads its contents (HTTP Response Body)
def get_data(url):
    try:
        # making request to the website
        req = urllib.request.Request(url=url)
        d = urllib.request.urlopen(req)

        # reading contents of the website
        return d.read()
    except Exception as ex:
        print("Exception in get_data : ",(str(ex)))


# Creating UDF for importing Data into mongoDB


#def import_content(filepath):
    #mng_client = pymongo.MongoClient('localhost', 27017)
    #mng_db = mng_client['Cars_data'] 
  #  collection_name = 'Data_test' 
    #db_cm = mng_db['Data_test']
    #cdir = os.path.dirname(os.path.abspath("__file__"))
    #file_res = os.path.join(cdir, filepath)

    #data = pd.read_csv(file_res)
   # data_json = json.loads(data.to_json(orient='records'))
   # db_cm.remove()
   # db_cm.insert_many(data_json)

from pymongo import MongoClient 
import pandas as pd 
client = MongoClient() 
db=client.Cars_test 
coll = db.Data_test 
df = pd.read_csv("/Users/shubh/OneDrive/Desktop/Clg_work/Trimester-2/Mongo/Mongo_Project/flask/file2.csv") #csv file which you want to import 
records_ = df.to_dict(orient = 'records') 
result = db.Data_test.insert_many(records_ ) 

# driver function
if __name__ == "__main__":
    app.run(debug=True)

