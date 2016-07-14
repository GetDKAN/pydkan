import sys
sys.path.append('..')

import os
import json
from dkan.client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')

if uri:
  api = DatasetAPI(uri, user, password, True)
  payload = {'parameters[type]': 'resource'}
  nodes = api.node(params=payload).json()
  resource = nodes[0]
  print resource
  csv = os.path.join('.', 'data', 'tension_sample_data.csv')
  # Attach the file to the resource node
  r = api.attach_file_to_node(csv, resource['nid'], 'field_upload')
  print r.status_code
  print r. text
  resource = api.node('retrieve', node_id=resource['nid'])
  print resource.json()['field_upload']
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'  