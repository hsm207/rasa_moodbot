from rasa.shared.nlu.training_data.formats.rasa_yaml import (RasaYAMLReader,
                                                             RasaYAMLWriter)

# imagine this is a file
nlu_file = """
version: "2.0"
nlu:
- synonym: Q144593
  examples: |
    - IBAN
    - iban
    - ibans
"""

yamlreader = RasaYAMLReader()
yamlwriter = RasaYAMLWriter()

# from file to rasa object
yamlreader.reads(nlu_file)

# from rasa object back to file
yamlwriter.dumps(yamlreader)

# check!
assert nlu_file.strip() == yamlwriter.dumps(yamlreader).strip()
