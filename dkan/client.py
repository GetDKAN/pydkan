import os
import json
import requests

class DatasetAPI:
  def __init__(self, dkan, user, password, debug=False):
    self.dkan = dkan
    self.headers = {
      'Accept': 'application/json',
    }
    self.cookies = {}
    self.debug = debug
    self.login(user, password)

  def login(self, user, password):
    uri = os.path.join(self.dkan, 'api/dataset/user/login')
    data = {
      'username': user,
      'password': password
    }
    # Login and set cookie
    login = self.post(uri, data=data)
    login = login.json()
    self.cookies = {
      login['session_name']: login['sessid'],
    }
    # Request token
    uri = os.path.join(self.dkan, 'services/session/token')
    token = self.post(uri)
    self.headers['X-CSRF-Token'] = token.text

  def node(self, node_id, action='retrieve', **kwargs):
    uri = os.path.join(self.dkan, 'api/dataset/node/%s' % node_id)
    action_map = {
      'retrieve': self.get,
      'update': self.put,
      'create': self.post,
      'delete': self.delete
    }
    if not action in action_map.keys():
      raise ValueError('action parameter should be one of the following: %s' % ', '.join(action_map.keys()))
    if action == 'retrieve':
      return action_map[action](uri)
    else:
      kwargs['headers'] = self.headers.copy()
      kwargs['headers']['Content-Type'] = 'application/json'
      return action_map[action](uri, **kwargs)

  def get(self, uri):
    return self.request(uri, 'GET')

  def post(self, uri, **kwargs):
    return self.request(uri, 'POST', **kwargs)

  def put(self, uri, **kwargs):
    return self.request(uri, 'PUT', **kwargs)

  def delete(self, uri, **kwargs):
    return self.request(uri, 'DELETE', **kwargs)

  def request(self, uri, rtype, **kwargs):
    if not 'headers' in kwargs.keys():
      kwargs['headers'] = self.headers    
    kwargs['cookies'] = self.cookies
    r = requests.Request(rtype, uri, **kwargs)
    prepared = r.prepare()
    if self.debug:
      DatasetAPI.pretty_print_request(prepared)
    s = requests.Session()
    return s.send(prepared)

  def attach_file_to_node(self, file, node_id, update=0):
    uri = os.path.join(self.dkan, 'api/dataset/node/%s/attach_file' % node_id)
    headers = self.headers.copy()
    data = {
      'field_name': 'field_upload',
      'attach': update,
    }
    files = {
      'files[1]': open(file, 'rb'),
    }
    return self.post(uri, headers=headers, data=data, files=files)

  @classmethod
  def pretty_print_request(cls, req):
    print('{}\n{}\n{}\n\n{}\n{}\n'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
        '------------END------------'
    ))
