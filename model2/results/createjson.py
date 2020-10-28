import pandas as pd
import json
import numpy as np
from sklearn import preprocessing

data= pd.read_table("../data/input_data.tsv")
le = preprocessing.LabelEncoder()
le.fit(data["propertyName"])

pred = pd.read_csv("../runs/1603810122/predictions.csv")
test_data["propertyName"] = le.inverse_transform(pred["Prediction"].astype(int))
final_test_df = pd.merge(test_data, data[["propertyId","propertyName","propertyDescription"]].drop_duplicates(),how="left", on="propertyName")

final_test_df.to_csv("output.tsv",sep="\t", index=False)
output = pd.read_table("output.tsv")


file1 = open('test-no-facts.json', 'r') 
file3 = open('test.json', 'w+') 



def default(obj):
    if type(obj).__module__ == np.__name__:
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj.item()
    raise TypeError('Unknown type:', type(obj))


count = 0
text_string = ""  
while True: 
    count += 1
    # Get next line from file 
    line = file1.readline()
    json_string = json.loads(line.strip())
    # if line is empty 
    # end of file is reached
    if not line: 
        break
    for i in range(len(json_string["passages"])):
        row_data = output[output["passageId"] == json_string["passages"][i]["passageId"]]
        print(json_string["passages"][i]["passageText"])
        print(row_data)
        new_dict = {"propertyId" : row_data["propertyId"].values[0], \
                    "propertyName" :row_data["propertyName"].values[0], \
                    "propertyDescription":row_data["propertyDescription"].values[0] }
        json_string["passages"][i]["exhaustivelyAnnotatedProperties"].append(new_dict)
    json_string = json.dumps(json_string, default=default)
    file3.write(json_string)
    file3.write("\n")

file1.close()
file3.close()