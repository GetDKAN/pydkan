import os
import json
from dkan.client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')

if uri:
  api = DatasetAPI(uri, user, password, True)
  data = {
      'title': 'Test Dataset',
      'type': 'dataset'
  }
  dataset = api.node('create', data=data)
  print dataset.status_code
  print dataset.text
  dataset = dataset.json()
  update = {
    'title': 'Test Dataset Updated',
  }
  r = api.node('update', node_id=dataset['nid'], data=update)
  print r.status_code
  print r.text
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'