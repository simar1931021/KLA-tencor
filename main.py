# this one is for the yaml file parsing

import yaml
with open("./Examples/Milestone1/Milestone1_Example.yaml") as file:
    data = yaml.load(file,Loader = yaml.FullLoader)
    print(data)




