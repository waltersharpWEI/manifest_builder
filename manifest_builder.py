#created by Walter on 2022/04/08 21:33
#The builder takes a directory as the input
#Then output a json manifest including all the files in the directory

#INPUT: the path to the directory that includes all the mesh files
#OUTPUT: a json string that includes all the file's filename
import os
import numpy as np
import json

def build_man(root_path):
    filename_list = []
    for filename in os.listdir(root_path):
        f = os.path.join(root_path, filename)
        if os.path.isfile(f):
            filename_list.append(filename)
    filename_list = np.array(filename_list)
    filename_list.sort()
    json_list = []
    for filename in filename_list:
        json_list.append({"filename":filename})
    return json_list

if __name__=="__main__":
    path = "E:\\volumetric\\dataset\\fvv\\BreakDancers\\TrackedMeshes"
    result = build_man(path)
    jsonStr = json.dumps(result)
    manifest_path = "manifest.json"
    with open(manifest_path,'w') as f1:
        f1.write(jsonStr)