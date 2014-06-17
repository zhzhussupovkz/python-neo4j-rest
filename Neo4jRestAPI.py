# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

class Neo4jRestAPI:
	api_url = ''

	def __init__(self, host, port):
		self.api_url = 'http://' + host + ':' + port + '/db/data'

	def get(self, url, headers):
		url = api_url + '/' + url
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		page = resp.read()
		return page

	def post(self, url, data, headers):
		data = urllib.urlencode(data)
		url = api_url + '/' + url
		req = urllib2.Request(url, data, headers = headers)
		resp = urllib2.urlopen(req)
		page = resp.read()
		return page

	def delete(self, url, headers):
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		req = urllib2.Request(url, None, headers = headers)
		req.get_method = lambda: "DELETE"
		resp = opener.open(req)
		page = resp.read()
		return page

	#cypher queries
	def cypher_query(self, query, params):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		data = {
			"query" : query,
			"params" : params,
		}
		page = self.post(url = 'cypher', data = data, headers = headers)
		return json.loads(page)

	#streaming
	def streaming(self):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"X-Stream" : "true",
		}
		page = self.get(url = '', headers = headers)
		return json.loads(page)

	#get property keys
	def propery_keys(self):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'properykeys', headers = headers)
		return json.loads(page)

	#create node
	def create_node(self, properties):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		page = self.post(url = 'node', data = properties, headers = headers)
		return json.loads(page)

	#get node
	def get_node(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'node/' + str(node_id), headers = headers)
		return json.loads(page)

	#delete node
	def delete_node(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.delete(url = 'node/' + str(node_id), headers = headers)
		return json.loads(page)

