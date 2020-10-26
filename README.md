
## Approach

The solution is inspired by How to [Fine-Tune BERT for Text Classification?](https://arxiv.org/abs/1905.05583)
I collected the bert-base-uncased model and train it with the data available.

## Installation

    pip install transformers torch torchvision

## Running the code

Ensure the train.json, test-no-facts.json are in the same folder as readdata.py and createjson.py

Run readdata.py to generate tsv files, then you can run the code in the notebook

Take output.tsv and process it with createjson.py, you will get test.json for the evalution

## Model Location

https://drive.google.com/file/d/1IOdTbBwcxJgDvjzkvN7SdkaFslVwcwn0/view?usp=sharing
