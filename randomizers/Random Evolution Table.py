# Almost all of this code is Aldo796

import UnityPy
import random
import os
from pathlib import Path

# make sure the file personal_masterdatas is in ../assets
# gamesettings is in Dpr/scriptableassets
os.chdir('../assets')
src = "personal_masterdatas"

env = UnityPy.load(src)

r = random.sample(range(1,561), 560)

i = 0

for obj in env.objects:
    if obj.type.name == "MonoBehaviour":
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "EvolveTable":
                for monID in tree['Evolve']:
                    monID["ar"] = [4, 0, r[i], 0, 1] 
                    i += 1
                #Saves the object tree
                obj.save_typetree(tree)

mod_folder = "../contents/010018E011D92000/romfs/Data/StreamingAssets/AssetAssistant/Pml"         
Path(mod_folder).mkdir(parents=True, exist_ok=True)
os.chdir(mod_folder)

with open("personal_masterdatas", "wb") as t:
    t.write(env.file.save(packer = (64,2)))
    


