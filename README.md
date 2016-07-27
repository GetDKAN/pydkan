# PyDKAN

This is a python client to interface with the [dkan_dataset_rest_api](https://github.com/NuCivic/dkan_dataset/tree/7.x-1.x/modules/dkan_dataset_rest_api) web service.

## Installation

```bash
# To install the latest of the latest
$ pip install git+git://github.com/NuCivic/pydkan.git@master#egg=pydkan
# To install a release
$ pip install git+git://github.com/NuCivic/pydkan.git@0.3#egg=pydkan
```

## Usage

```python
>>> from dkan.client import DatasetAPI
>>> user, password = ("admin", "admin")
>>> uri = "http://docker:32770"
>>> api = DatasetAPI(uri, user, password)
>>> print api.node('index').json()
[{u'status': u'1', u'comment': u'0', u'vid': u'34', u'changed': u'1468526087', u'uid': u'1', u'language': u'und', u'title': u'Test Dataset', u'translate': u'0', u'created': u'1468526087', u'uri': u'http://docker:32770/api/dataset/node/26', u'nid': u'26', u'sticky': u'0', u'promote': u'0', u'type': u'dataset', u'tnid': u'0', u'uuid': u'9ba2afca-929d-429b-9274-dcd2ce4fc195'}, {u'status': u'1', u'comment': u'0', u'vid': u'5', u'changed': u'1468526063', u'uid': u'1', u'language': u'und', u'title': u'Madison Polling Places', u'translate': u'0', u'created': u'1360559790', u'uri': u'http://docker:32770/api/dataset/node/5', u'nid': u'5', u'sticky': u'0', u'promote': u'0', u'type': u'resource', u'tnid': u'0', u'uuid': u'1f247b5e-678d-4622-a9e0-b6ee49891772'}, {u'status': u'1', u'comment': u'1', u'vid': u'35', u'changed': u'1468592943', u'uid': u'1', u'language': u'und', u'title': u'Wisconsin Polling Places', u'translate': u'0', u'created': u'1360559620', u'uri': u'http://docker:32770/api/dataset/node/4', u'nid': u'4', u'sticky': u'0', u'promote': u'0', u'type': u'dataset', u'tnid': u'0', u'uuid': u'9340b03b-dd72-4a2f-a614-cd2a2c052d1b'}, {u'status': u'1', u'comment': u'0', u'vid': u'7', u'changed': u'1468606278', u'uid': u'1', u'language': u'und', u'title': u'1-2012-Foreclosures-by-State', u'translate': u'0', u'created': u'1360558980', u'uri': u'http://docker:32770/api/dataset/node/7', u'nid': u'7', u'sticky': u'0', u'promote': u'0', u'type': u'resource', u'tnid': u'0', u'uuid': u'ed3c4995-db6b-494b-af0e-7d8e54268829'}, {u'status': u'1', u'comment': u'1', u'vid': u'36', u'changed': u'1468604008', u'uid': u'1', u'language': u'und', u'title': u'US National Foreclosure Statistics January 2012', u'translate': u'0', u'created': u'1360557746', u'uri': u'http://docker:32770/api/dataset/node/6', u'nid': u'6', u'sticky': u'0', u'promote': u'0', u'type': u'dataset', u'tnid': u'0', u'uuid': u'37aa88e1-7cf4-4d79-9102-8127e64ea9b3'}, {u'status': u'1', u'comment': u'0', u'vid': u'9', u'changed': u'1357269434', u'uid': u'1', u'language': u'und', u'title': u'Table of Gold Prices', u'translate': u'0', u'created': u'1360555641', u'uri': u'http://docker:32770/api/dataset/node/9', u'nid': u'9', u'sticky': u'0', u'promote': u'0', u'type': u'resource', u'tnid': u'0', u'uuid': u'1821de04-06da-4d5e-b47f-10d943a50889'}, {u'status': u'1', u'comment': u'1', u'vid': u'14', u'changed': u'1466167593', u'uid': u'1', u'language': u'und', u'title': u'Gold Prices in London 1950-2008 (Monthly)', u'translate': u'0', u'created': u'1360555545', u'uri': u'http://docker:32770/api/dataset/node/8', u'nid': u'8', u'sticky': u'0', u'promote': u'0', u'type': u'dataset', u'tnid': u'0', u'uuid': u'748d192c-f2cf-4ef1-a11a-5cde695df4da'}, {u'status': u'1', u'comment': u'0', u'vid': u'1', u'changed': u'1357269426', u'uid': u'1', u'language': u'und', u'title': u'About', u'translate': u'0', u'created': u'1357935656', u'uri': u'http://docker:32770/api/dataset/node/1', u'nid': u'1', u'sticky': u'0', u'promote': u'0', u'type': u'page', u'tnid': u'0', u'uuid': u'b1c65dd7-80b9-4f7f-a7ce-edb5f51a590e'}, {u'status': u'1', u'comment': u'0', u'vid': u'3', u'changed': u'1357269428', u'uid': u'1', u'language': u'und', u'title': u'Geospatial Data Explorer Examples', u'translate': u'0', u'created': u'1357278812', u'uri': u'http://docker:32770/api/dataset/node/3', u'nid': u'3', u'sticky': u'0', u'promote': u'0', u'type': u'group', u'tnid': u'0', u'uuid': u'277430d8-f267-48ae-b670-cf52273fc96b'}, {u'status': u'1', u'comment': u'0', u'vid': u'2', u'changed': u'1357269427', u'uid': u'1', u'language': u'und', u'title': u'Data Explorer Examples', u'translate': u'0', u'created': u'1357269426', u'uri': u'http://docker:32770/api/dataset/node/2', u'nid': u'2', u'sticky': u'0', u'promote': u'0', u'type': u'group', u'tnid': u'0', u'uuid': u'9e36b11d-41b7-4fc2-8dea-43746f7671e5'}, {u'status': u'1', u'comment': u'1', u'vid': u'15', u'changed': u'1466167593', u'uid': u'1', u'language': u'und', u'title': u'Afghanistan Election Districts', u'translate': u'0', u'created': u'1351612344', u'uri': u'http://docker:32770/api/dataset/node/10', u'nid': u'10', u'sticky': u'0', u'promote': u'0', u'type': u'dataset', u'tnid': u'0', u'uuid': u'af645ea8-2ddb-416c-9930-ce50f2949159'}, {u'status': u'1', u'comment': u'0', u'vid': u'11', u'changed': u'1357269436', u'uid': u'1', u'language': u'und', u'title': u'District Names', u'translate': u'0', u'created': u'1351485646', u'uri': u'http://docker:32770/api/dataset/node/11', u'nid': u'11', u'sticky': u'0', u'promote': u'0', u'type': u'resource', u'tnid': u'0', u'uuid': u'be55ed21-afe0-48d7-8021-79a6e95a8cc9'}]
>>> data = {"title": "new node"}
>>> print api.node('create', data=data).json()
[{u'nid': u'10', u'uri': u'http://docker:32770/node/10'}]
>>> print api.node('delete', node_id=10)
[true]
```
Check the examples folder, there are snippets for pretty much everything you can do with this library.
