	
## Approach

-   A C-LSTM classifier. See clstm_classifier.py. Reference: [A C-LSTM Neural Network for Text Classification](https://arxiv.org/abs/1511.08630).

## Installation

Create ***virtualenv***
```pip install "tensorflow==1.15" pandas numpy```

## Running the code

- Place the json files into data folder, Run ```python readdata.py``` to generate tsv files

- Run this for building the model, ``` python train.py --data_file=./data/data.csv --clf=lstm --decay_steps=5000 ```
- Run this for creating the test result, ```python test.py --test_data_file=./data/data.csv --run_dir=./runs/1603810122 --checkpoint=clf-5000```
- Go to the results folder, run ```python createjson.py```, you will get test.json for the evalution
-  For result testing, download the model from google drive, place the runs folder in the project directory and run the test code above

## Model Location

https://drive.google.com/file/d/1OLpswOJ6FMsAcfO0HtgC7JMnV5E19V9e/view?usp=sharing
