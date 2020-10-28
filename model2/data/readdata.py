import json
import pandas as pd
from sklearn import preprocessing

file1 = open('train.json', 'r') 
file2 = open("input_data.tsv", "w")
file2.write("propertyId" + "\t" + "propertyName" + "\t" + "propertyDescription" + "\t" + "passageText")
file2.write("\n")

count = 0
text_string = ""  
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline()
  
    # if line is empty 
    # end of file is reached
    if not line: 
        break
    text_string = json.loads(line.strip())["passages"][0]["exhaustivelyAnnotatedProperties"][0]["propertyId"] + "\t" + \
                  json.loads(line.strip())["passages"][0]["exhaustivelyAnnotatedProperties"][0]["propertyName"] + "\t" + \
                  json.loads(line.strip())["passages"][0]["exhaustivelyAnnotatedProperties"][0]["propertyDescription"] + "\t" + \
                  json.loads(line.strip())["passages"][0]["passageText"]

    file2.write(text_string)
    file2.write("\n")
    text_string = ""


file1.close()
file2.close()

file1 = open('test-no-facts.json', 'r') 
file2 = open("test_data.tsv", "w")
file2.write("passageText"+"\t"+"passageId")
file2.write("\n")

count = 0
text_string = ""  
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline()
  
    # if line is empty 
    # end of file is reached
    if not line: 
        break
    for i in range(len(json.loads(line.strip())["passages"])):
        text_string = json.loads(line.strip())["passages"][i]["passageText"] + "\t" + json.loads(line.strip())["passages"][i]["passageId"]
        file2.write(text_string)
        file2.write("\n")
        text_string = ""


file1.close()
file2.close()


data= pd.read_table("data/input_data.tsv")
le = preprocessing.LabelEncoder()
data["label"] = le.transform(data["propertyName"])
data.rename(columns={"passageText":"content"}, inplace=True)
data.to_csv("data/input_data.csv",index=False)
test_data= pd.read_table("data/test_data.tsv")
test_data.rename(columns={"passageText":"content"}, inplace=True)
test_data.to_csv("data/test_data.csv",index=False)