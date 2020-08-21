import json
import pickle


with open('Audi80.json') as f:
    reader = json.load(f)
    rows = str(reader)

with open('Audi100.pickle', 'wb') as f:
    pickle.dump(rows, f)