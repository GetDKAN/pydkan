# -*- coding: utf-8 -*-

"""
dkan.client
~~~~~~~~~~~~~~~~~

This module contains the available client for dkan's apis.
"""

import os
import json
import requests

class DatasetAPI:
  """The DKAN Dataset REST api client

  Provides a client for all available methods provided by the dkan
  dataset rest api (Based on drupal services). It uses the requests
  library for all the heavy lifting.

  :param dkan: The DKAN site's url
  :param user: The drupal user to authenticate against the api.
  :param password: The drupal password to authenticate against the api
  :param debug: Whether the client pretty prints the raw POST requests
                to stdout or not

  Usage::

    >>> from dkan.client import DatasetAPI
    >>> uri = "http://dkan"
    >>> user, password = ('admin', 'admin')
    >>> api = DatasetAPI(uri, user, password)
  """
  def __init__(self, dkan, user, password, debug=False):
    self.dkan = dkan
    self.headers = {
      'Accept': 'application/json',
    }
    self.cookies = {}
    self.debug = debug
    self.login(user, password)

  def login(self, user, password):
    """Authenticates against the dkan site.

    This method should not be called from user code. It authenticate
    against the drupal site in two steps. 1) it posts the user and password
    to api/dataset/user/login and retrieves a cookie 2) it sets the acquired
    cookie and posts against services/sessions/token to retrieve a token
    that's going to be sent as a header for every request this client
    builds.


    :param user: Drupal user
    :param password: Drupal Password
    """
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

  def node(self, action='index', **kwargs):
    """Interface to the node endpoint.

    This method builds requests against the api/dataset/node endpoint. It is
    simply a function that creates a match between actions and http requests
    types.
    index -> Builds a GET request againts api/dataset/node
    create -> Builds a POST request against api/dataset/node
    retrieve -> Builds a GET request against api/dataset/node/<nid> where nid
                is an existing node's id
    update -> Builds a PUT request against api/dataset/node/<nid> where nid
              is an existing node's id
    delete -> Builds a DELETE request against api/dataset/node/<nid> where nid
              is an existing node's id

    :param action: This is either index, create, retrieve, update or delete
    :param node_id: (optional) the node id that needs to be
                    retrieved/updated/deleted
    :param data: (optional) a dictionary representing POST/PUT parameters
    :param params: (optional) a dictionary representing GET parameters
    :param headers: (optional) a dictionary representing http request headers

    """
    uri = os.path.join(self.dkan, 'api/dataset/node')
    if action not in ['index', 'create']:
      node_id = kwargs.get('node_id', False)
      if node_id:
        del kwargs['node_id']
        uri = os.path.join(uri, '%s' % node_id)
      else:
        raise ValueError('For action type %s you need to specify a node_id' % action)
    action_map = {
      'index': self.get,
      'retrieve': self.get,
      'update': self.put,
      'create': self.post,
      'delete': self.delete
    }
    if not action in action_map.keys():
      raise ValueError('action parameter should be one of the following: %s' % ', '.join(action_map.keys()))
    if action not in ['index', 'retrieve']:
      kwargs['headers'] = self.headers.copy()
      kwargs['headers']['Content-Type'] = 'application/json'
      if 'data' in kwargs.keys():
        kwargs['data'] = json.dumps(kwargs['data'])
    return action_map[action](uri, **kwargs)

  def get(self, uri, **kwargs):
    return self.request(uri, 'GET', **kwargs)

  def post(self, uri, **kwargs):
    return self.request(uri, 'POST', **kwargs)

  def put(self, uri, **kwargs):
    return self.request(uri, 'PUT', **kwargs)

  def delete(self, uri, **kwargs):
    return self.request(uri, 'DELETE', **kwargs)

  def request(self, uri, rtype, **kwargs):
    """Builds a raw requests using the requests library

    :param uri: The URI for the http request
    :rtype: GET/POST/PUT/DELETE
    """
    if not 'headers' in kwargs.keys():
      kwargs['headers'] = self.headers    
    kwargs['cookies'] = self.cookies
    r = requests.Request(rtype, uri, **kwargs)
    prepared = r.prepare()
    if self.debug:
      DatasetAPI.pretty_print_request(prepared)
    s = requests.Session()
    return s.send(prepared)

  def attach_file_to_node(self, file, node_id, field, update=0):
    """ Uploads and attach a file to a specific node

    :param file: A path to a file
    :param node_id: The node id that we'll attach to the file to
    :param field: The name of the drupal file field
    :param update: (optional) 0 -> replace existing, 1 -> attach a new one
    """
    uri = os.path.join(self.dkan, 'api/dataset/node/%s/attach_file' % node_id)
    headers = self.headers.copy()
    data = {
      'field_name': field,
      'attach': update,
    }
    files = {
      'files[1]': open(file, 'rb'),
    }
    return self.post(uri, headers=headers, data=data, files=files)

  @classmethod
  def pretty_print_request(cls, req):
    """Pretty prints a request object

    :param req: the http request object
    """
    print('{}\n{}\n{}\n\n{}\n{}\n'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
        '------------END------------'
    ))
