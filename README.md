# Capstone-Project-5e-Analysis
The purpose of this repo is to serve as a centralised repository for all the code and files for my capstone project. This project's purpose is to utalize key aspects of a DnD 5e monster in order to construct a model and predict its core stat block. It goes from start to finish of a machine learning pipeline, with gathering data, cleaning and exploring it, then constucting and fine tuning the model. Further information and findings of the project, as well as the souce of my data can be located bellow:

Overleaf: https://www.overleaf.com/read/hvpqwrwhrbwz 

Datasource: http://www.dnd5eapi.co/ 



Bellow you can find a summarization of the modules included in this repo.

## Extract_Monster_Data.py
This file is the code I wrote in order to access the api that help my data and export it to a readable .json format.

## Clean_Monster_Data.py
The purpose of this file was to extract the needed/useful info from the dumped json and make it nice and readable for a pandas dataframe to work with.

## ExploratoryAnalysis.ipynb
This notebokk was where I performed my exploratory analysis of my data.

## Model_Construction.ipynb
This was the jupyter notebook used to actually test algorithms and build my model.

## Monster_Data_Raw
The json dump from the api.

## MonsterData.csv
The cleaned data file.









