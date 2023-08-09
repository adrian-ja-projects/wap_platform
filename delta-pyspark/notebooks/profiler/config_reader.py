import yaml

class YamlConfigReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_yaml_file(self):
        with open(self.file_path) as f:
            try:
                profilerconfig = yaml.safe_load(f)
                return profilerconfig
            except yaml.YAMLError as e:
                print(e)