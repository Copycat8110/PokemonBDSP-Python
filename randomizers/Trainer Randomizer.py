# Almost all of this code is Aldo796

import UnityPy
import random
# import glob
import os
import json
from pathlib import Path

# all of the following would work
os.chdir('../assets')
src = "masterdatas"

env = UnityPy.load(src)
extract_dir = "Walker"

i = 0
MaxString = ""
for obj in env.objects:
    i+=1
#     # print(i)
    if obj.type.name == "MonoBehaviour":

        # edit
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()

            #TrainerPoke
            if tree['m_Name'] == "TrainerTable":
                for dic in tree['TrainerPoke']:
                    pokeList = []
                    MaxString += str(dic["ID"]) + ", "
                    for pokeNum in range(1, 7):
                        # print(dic["P"f"{pokeNum}Level"])
                        level = dic["P"f"{pokeNum}Level"]
                        if level > 0:
                            pokeList.append(level)
                            #Increases level by 50% with a cap at level 100
                            dic["P"f"{pokeNum}Level"] = int(dic["P"f"{pokeNum}Level"] * 1.5)
                            if dic["P"f"{pokeNum}Level"] > 100:
                                dic["P"f"{pokeNum}Level"] = 100
                            newPokemon = random.randint(1,493)
                            dic["P"f"{pokeNum}MonsNo"] = newPokemon
                            ##Moves 1 through 4
                            dic["P"f"{pokeNum}Waza1"] = 52
                            dic["P"f"{pokeNum}Waza2"] = 52
                            dic["P"f"{pokeNum}Waza3"] = 52
                            dic["P"f"{pokeNum}Waza4"] = 52
                            """            
                            "P1TalentHp": 0,
                            "P1TalentAtk": 0,
                            "P1TalentDef": 0,
                            "P1TalentSpAtk": 0
                            "P1TalentSpDef": 0,
                            "P1TalentAgi": 0,
                            """
                            #Set all IVs to 31 for maximum difficulty :P
                            dic["P"f"{pokeNum}TalentHp"] = 31
                            dic["P"f"{pokeNum}TalentAtk"] = 31
                            dic["P"f"{pokeNum}TalentDef"] = 31
                            dic["P"f"{pokeNum}TalentSpAtk"] = 31
                            dic["P"f"{pokeNum}TalentSpDef"] = 31
                            dic["P"f"{pokeNum}TalentAgi"] = 31
                
                
                    # if len(pokeList) > 0:
                    #     MaxString += f"{min(pokeList)}, " + f"{max(pokeList)}, " + pypokedex.get(dex=dic["P1MonsNo"]).name + ", " f"{len(pokeList)}\n"
                    # else:
                    #     print("No Pokemon")
                    # for key in dic.keys():
                    #     if type(dic[key]) != int and type(dic[key]) != str:
                    #         for mon in i[key]:
                    #              if type(mon) == dict:
                    #                 if "monsNo" in mon.keys():
                    #                     if mon['monsNo'] != 0:
                    #                         mon['monsNo'] = random.randint(1,493)

                # print(tree)
                obj.save_typetree(tree)
                # name = tree['m_Name']
                # data = str(obj.read())
                # fp = os.path.join(extract_dir, f"{name}.json")
                # with open(fp, "wt", encoding = "utf8") as f:
                #     json.dump(tree, f, ensure_ascii = False, indent = 4)
            # print(str(i) + ": " + str(tree))
            # apply modifications to the data within the tree
                
                
                
# saving an edited file
# apply modifications to the objects
# don't forget to use data.save()
    # ...
    # 
    #
mod_folder = "../contents/010018E011D92000/romfs/Data/StreamingAssets/AssetAssistant/Dpr"         
Path(mod_folder).mkdir(parents=True, exist_ok=True)
os.chdir(mod_folder)
    
with open("masterdatas", "wb") as f:
    f.write(env.file.save(packer = (64,2)))
