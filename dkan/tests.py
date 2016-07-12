import os, unittest
from client import DatasetAPI

class TestDatasetAPI(unittest.TestCase):
    def setUp(self):
        uri = os.environ.get('DKAN_URI', False)
        user = os.environ.get('DKAN_USER', 'admin')
        password = os.environ.get('DKAN_PASSWORD', 'admin')
        # Fail if DKAN_URI is not set
        if not uri:
            self.skipTest(TestDatasetAPI)
        self.api = DatasetAPI(uri, user, password)
        self.cleanup = []

    def tearDown(self):
        self.cleanup = list(set(self.cleanup))
        for node in self.cleanup:
            delete = self.api.node('delete', node_id=node)
            self.assertEqual(delete.status_code, 200)
        self.cleanup = []

    def _get_nodes_of_type(self, node_type):
        payload = {
            'parameters[type]': node_type
        }
        r = self.api.node(params=payload)
        self.assertEqual(r.status_code, 200)
        return r.json()

    def _get_nodes_types(self, nodes):
        types = [dataset['type'] for dataset in nodes]
        types = list(set(types))
        return types

    def _test_list_nodes(self, node_type):
        nodes = self._get_nodes_of_type(node_type)
        types = self._get_nodes_types(nodes)
        # Test for dataset type
        self.assertEqual(types[0], node_type)
        self.assertEqual(len(types), 1)

    def test_list_datasets(self):
        self._test_list_nodes('dataset')

    def test_list_resources(self):
        self._test_list_nodes('resource')

    def _test_create_node(self, data):
        node_type = data['type']
        nodes = self._get_nodes_of_type(node_type)
        original_count = len(nodes)
        # Create Node
        node = self.api.node('create', data=data)
        self.assertEqual(node.status_code, 200)
        node = node.json()
        self.cleanup.append(node['nid'])
        # Verify count
        nodes = self._get_nodes_of_type(node_type)
        new_count = len(nodes)
        self.assertEqual(new_count, original_count + 1)
        return node

    def test_create_dataset(self):
        data = {
            'title': 'Test Dataset',
            'type': 'dataset',
            'body': [
                {
                    'value': "Body for test Dataset",
                },
            ]
        }
        self._test_create_node(data)

    def test_create_resource(self):
        data = {
            'title': 'Test Resource',
            'type': 'resource',
            'body': [
                {
                    'value': "Body for test Resource",
                },
            ]
        }
        self._test_create_node(data)

    def _test_update_node(self, data):
        original_node = self._test_create_node(data)
        original_node = self.api.node('retrieve', node_id=original_node['nid']).json()
        update = {
            'title': '%s updated' % data['title'],
        }
        self.assertTrue('nid' in original_node.keys())
        node = self.api.node('update', node_id=original_node['nid'], data=update)
        self.assertEqual(node.status_code, 200)
        node = self.api.node('retrieve', node_id=original_node['nid']).json()
        self.assertEqual('%s updated' % original_node['title'], node['title'])

    def test_update_dataset(self):
        data = {
            'title': 'Test Dataset to be updated',
            'type': 'dataset',
            'body': [
                {
                    'value': "Body for test Dataset",
                },
            ]
        }
        self._test_update_node(data)

    def test_update_resource(self):
        data = {
            'title': 'Test Resource to be updated',
            'type': 'resource',
            'body': [
                {
                    'value': "Body for test Resource",
                },
            ]
        }
        self._test_update_node(data)

    def test_attach_file_to_resource(self):
        csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                           'examples', 'data', 'tension_sample_data.csv')
        data = {
            'title': 'Test Resource to receive a file',
            'type': 'resource',
            'body': [
                {
                    'value': "Body for test Resource",
                },
            ]
        }
        resource = self._test_create_node(data)
        resource = self.api.node('retrieve', node_id=resource['nid']).json()
        r = self.api.attach_file_to_node(csv, resource['nid'], 'field_upload')
        self.assertEqual(r.status_code, 200)
        resource = self.api.node('retrieve', node_id=resource['nid']).json()
        filename = resource['field_upload']['und'][0]['filename']
        self.assertTrue(filename=='tension_sample_data.csv')

    def _test_delete_node(self, data):
        count = len(self._get_nodes_of_type(data['type']))
        node = self._test_create_node(data)
        self.assertTrue('nid' in node.keys())
        delete = self.api.node('delete', node_id=node['nid'])
        self.assertEqual(delete.status_code, 200)
        self.cleanup.remove(node['nid'])
        new_count = len(self._get_nodes_of_type(data['type']))
        self.assertEqual(count, new_count)

    def test_delete_dataset(self):
        data = {
            'title': 'Test Dataset to be deleted',
            'type': 'dataset',
            'body': [
                {
                    'value': "Body for test Dataset",
                },
            ]
        }
        self._test_delete_node(data)

    def test_delete_resource(self):
        data = {
            'title': 'Test Resource to be deleted',
            'type': 'resource',
            'body': [
                {
                    'value': "Body for test Resource",
                },
            ]
        }
        self._test_delete_node(data)

if __name__ == '__main__':
    unittest.main()
