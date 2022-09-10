# Car-Specification-Analysis

# Introduction : -
This project is based on cars data from [auto-data.net]https://www.auto-data.net/en/ which is a place for buyers to sell all major minor features / specifications cars 
across World. Lots of people think to buy a luxiers cars but dont know all the specifications about it. It might be any brand of car. So we have got a solution for it, 
by using the mongoDB and visualization techniques we can show them which car(specification wise) is better than others.

# WHAT IS THE PROJECT ABOUT: -
The project aimed at providing in depth details of the cars to a potential customer to help them identify and  broader the perspective while buying the car.
The end goal of this project is to clean the data as much as possible and storing it in the MongoDB for the potential customer
The Target audience for this project are Car dealer , Car enthusiast 

# Technical architecture : -
<img width="592" alt="arch" src="https://user-images.githubusercontent.com/108860622/189486409-6d9cd6e7-b238-44e4-b819-b7eb58e1a670.png">

# Methodologies : -

# 1: Data Collection Methodologies :- 
* Google Forms / API / Web Scrapping:- <br>
Web Scraping refers to the process of extracting data from a website or specific webpage. This can be done either manually or by using software tools called web scrapers. We have done it manually in this project.

* Website providing the data :- <br>
https://www.auto-data.net/en/

* Method: API/ Scrapping the data:- <br>
We have created a function for data scrapping using Flask framework

# 2: Data Storing Methodologies : -
* No of Transformations applied:- <br> 2(pandas data frame & Json)
* Pre-Transformation Strategies :- <br>Pandas Data frame
* Post-Transformation Strategies:- <br>Json file

# Description of working module: -

 Importing all required libraries and tools. 
 Establish a connection with Mongo DB localhost.
 After importing the prerequisites, The user defined function called generate_json 
 gets called for fetching the given URL.
 Generate_json function sends a request and gets the data and the response from the given URL which
 is where the get_data function is called.
 Get_data function gets the metadate and sends all the data to the return value into a variable for parsing.
 As the  HTML parser collects the data from the given data, The fetched noisy data is converted into a pandas data frame in a dictionary format.
 The pandas dataframe data cleaning methods removes the noise from the data.
 with the help of jsonify , to_json function is called and the data frame data is dumped into a Json file named temp.
 The function dump data is the function that injects clean data from Json file into the Mongo DB.
 After successful injection, the message will be shown as Data inserted successful











