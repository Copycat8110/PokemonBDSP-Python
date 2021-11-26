import UnityPy
import random
import os
from pathlib import Path

# make sure the file gamesettings is in this folder
# gamesettings is in Dpr/scriptableassets
os.chdir('../assets')
src = "gamesettings"

env = UnityPy.load(src)

for obj in env.objects:
    if obj.type.name == "MonoBehaviour":
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()
            
            ##Two encounter tables are named FieldEncountTable_d (diamond) and FieldEncountTable_p (pearl)
            if tree['m_Name'] == "FieldEncountTable_d" or tree['m_Name'] == "FieldEncountTable_p":
                for area in tree['table']:
                    for key in area.keys():
                        if type(area[key]) == list:
                            if type(area[key]) == dict:
                                for mon in area[key]:
                                    if mon['monsNo'] != 0:
                                        mon['monsNo'] = random.randint(1,493)
                #Saves the object tree
                obj.save_typetree(tree)
                # apply modifications to the data within the tree
                
                
                
# saving an edited file
# apply modifications to the objects
# don't forget to use data.save()
    # ...
    # 
    # 
#This output is compressed, :DDDDDD!!!

mod_folder = "../contents/010018E011D92000/romfs/Data/StreamingAssets/AssetAssistant/Dpr/scriptableassets"         
Path(mod_folder).mkdir(parents=True, exist_ok=True)
os.chdir(mod_folder)

with open("gamesettings", "wb") as f:
    f.write(env.file.save(packer = (64,2)))
