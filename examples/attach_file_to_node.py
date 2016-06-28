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

# Attach the file to the resource node
r = api.attach_file_to_node(CSV, RESOURCE_ID)
print r.status_code
print r. text