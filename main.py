# this one is for the yaml file parsing

import yaml
with open("Milestone1/Milestone1A.yaml") as file:
    data = yaml.load(file,Loader = yaml.FullLoader)
    print(data)





