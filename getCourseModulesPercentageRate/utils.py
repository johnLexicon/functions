import json
from .data import json_string

data = json.loads(json_string)

def get_modules_names():
  names = []
  for module in data['modules']:
    names.append(module['name'])
  return names

def get_total_weeks():
  total = 0
  for m in data['modules']:
    total += m['weeks']
  return total

def get_coursemodule_percentage(moduleName):
  try:
    module = next(m for m in data['modules'] if m['name'] == moduleName)
    total_weeks = get_total_weeks()
  except:
    return None

  return module['weeks'] / total_weeks * 100