import sys
sys.path.append('..')

import os
import json
from dkan.client import DatasetAPI

DKAN_URI = 'http://docker:32782'
RESOURCE_ID = 5
CSV = os.path.join('/Users/teofilosibileau/Downloads', 'CSV.csv')

# Make the api authenticate properly
api = DatasetAPI(
  DKAN_URI,
  'admin',
  'admin',
  True
)

# Get the resource node which file we want to update
resource = api.node(RESOURCE_ID, 'retrieve')
resource = resource.json()

# Check if the field for the file is empty.
if type(resource['field_upload']) != list:
  # If it's not empty the field
  data = {
    'field_upload': {
      'und': [{}],
    },
  }
  data = json.dumps(data)
  r = api.node(RESOURCE_ID, 'update', data=data)
  print r.status_code
  print r.text

# Attach the file to the resource node
r = api.attach_file_to_node(CSV, RESOURCE_ID)
print r.status_code
print r. text