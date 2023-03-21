
"""
This program will read the smoker temperatures and push the information to Rabbit MQ Server
Gabbs Albrecht
02/27/2023
"""


#imports at top of module
import requests as rq
import ast
import json

#defing variables
base_URL = "https://www.dnd5eapi.co"
list_URL ="/api/monsters"
output_file = "Monster_Data_Raw.json"
output = []

#Getting the index of spells from the API
requestInfo =  rq.get(base_URL + list_URL)


#format returned by the api is funky so this transforms it into just a list of dictionaries to work with
Monster_List_Pull = ast.literal_eval(requestInfo.text)
Monster_List = Monster_List_Pull['results']



def main():
    
  
    
    for x in Monster_List:
        Monster_Index = Monster_List.index(x)
        Monster_Acting = Monster_List[Monster_Index]
        Monster_Dict_Index = Monster_Acting['url']
        Monster_Info =  rq.get(base_URL + Monster_Dict_Index).text

        print(Monster_Info)
        processed = json.loads(Monster_Info)
        output.append(processed)



    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4)



#Standard python idiom that let's us run our code as a script
if __name__ == "__main__":
    
    main()