import yaml

class YamlConfigParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_yaml(self):
        with open(self.file_path) as f:
            try:
                profilerconfig = yaml.safe_load(f)
                print(profilerconfig)
            except yaml.YAMLError as e:
                print(e)

    def 

    