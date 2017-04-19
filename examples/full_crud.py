import os
import json
from client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')

if uri:
    api = DatasetAPI(uri, user, password, True)
    # Create dataset
    print 'CREATE DATASET'
    data = {
        'title': 'Test Dataset',
        'type': 'dataset'
    }
    r = api.node('create', data=data)
    print 'Response: %s\n\n' % r.text
    dataset_nid = r.json()['nid']
    # Create resource
    print 'CREATE RESOURCE'
    data = {
        'title': 'Test Resource',
        'type': 'resource',
        'field_dataset_ref': {
            'und': {
                'target_id': dataset_nid,
            },
            
        },
    }
    r = api.node('create', data=data)
    print 'Response: %s\n\n' % r.text
    resource_nid = r.json()['nid']
    # Retrieve parent node to see if resource_ref has been created
    print 'RETRIEVE PARENT DATASET TO CHECK REFERENCE'
    r = api.node('retrieve', node_id=dataset_nid)
    print 'Response: %s\n' % r.text
    resource_ref = r.json()['field_resources']['und'][0]['target_id']
    print 'Dataset -> Resource reference is %s\n\n' % resource_ref
    # Update dataset title
    data = {
        'title': 'Updated dataset title'
    }
    r = api.node('update', node_id=dataset_nid, data=data)
    print 'Response: %s\n\n' % r.text
    # Attach file to resource
    csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.',
                     'data', 'tension_sample_data.csv')
    print 'ADD FILE TO RESOURCE'
    r = api.attach_file_to_node(csv, resource_nid, 'field_upload')
    print 'Response: %s\n\n' % r.text
    # Retrieve updated resource
    print 'RETRIEVE RESOURCE TO CHECK FILE UPLOAD'
    r = api.node('retrieve', node_id=resource_nid)
    print 'Response: %s\n\n' % r.text
else:
    print 'Please Set the dkan URL as an ENVIRONMENT variable'