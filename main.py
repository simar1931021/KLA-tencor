# this one is for the yaml file parsing

import yaml
class yamlParser:
    def prs(self):
        with open("Milestone1/Milestone1A.yaml") as file:
            data = yaml.load(file,Loader = yaml.FullLoader)
            return data






