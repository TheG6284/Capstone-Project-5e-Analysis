import csv
import pandas as pd
import json


with open('Monster_Data_Raw.json') as json_file:
    start_data = json.load(json_file)

monsterDataHeader = ['Index','Type', 'HP', 'AC', 'Size','STR', 'DEX', 'CON', 'INT', 'WIS', 'CHAR', 'CR']
outfile = 'MonsterData.csv'

monsterDataRow = []


monster_df = pd.DataFrame(columns = monsterDataHeader)

def dataNumerizer(column_name):
    
    strings = column_name.unique()
    strings = strings.tolist()
    assoc_dict = {}
    size_list = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']
    if strings[0] in size_list:
        strings = size_list
        
    for x in strings:
        assoc_dict["{}".format(x)] = strings.index(x) +1
    
    return assoc_dict



for x in start_data:
    monsterDataRow = [x['index'], x['type'], x['hit_points'], x['armor_class'][0]['value'], x['size'], x['strength'],x['dexterity'], x['constitution'], x['intelligence'], x['wisdom'], x['charisma'], x['challenge_rating']]
    #monster_df.loc[len(monster_df)] = monsterDataRow 
    monster_df = monster_df.append(pd.DataFrame([monsterDataRow], columns=monsterDataHeader), ignore_index=True)

monster_df['Size'] = monster_df['Size'].map(dataNumerizer(monster_df['Size']))
monster_df['Type'] = monster_df['Type'].map(dataNumerizer(monster_df['Type']))

print(monster_df.head(5))

monster_df.to_csv(outfile, index = False)