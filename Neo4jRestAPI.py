# -*- coding: utf-8 -*-
#
# Neo4jRestAPI class
#
# @author zhzhussupovkz@gmail.com
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Zhussupov Zhassulan zhzhussupovkz@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import urllib
import urllib2
import json

class Neo4jRestAPI:
	api_url = ''

	def __init__(self, host, port):
		self.api_url = 'http://' + host + ':' + port + '/db/data'

	def get(self, url, headers):
		url = self.api_url + '/' + url
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		page = resp.read()
		return page

	def post(self, url, data, headers):
		data = urllib.urlencode(data)
		url = self.api_url + '/' + url
		req = urllib2.Request(url, data, headers = headers)
		resp = urllib2.urlopen(req)
		page = resp.read()
		return page

	def delete(self, url, headers):
		url = self.api_url + '/' + url
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

	#get relationship by id
	def get_relationship(self, rel_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'relationship/' + str(rel_id), headers = headers)
		return json.loads(page)

	#create relationship
	def create_relationship(self, from_id, to_id, type, data):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		data = {
			"to" : self.api_url + 'node/' + str(to_id),
			"type" : type,
			"data" : data,
		}
		page = self.post(url = 'node/' + str(from_id) + '/relationships', data = data, headers = headers)
		return json.loads(page)

	#delete relationship
	def delete_relationship(self, rel_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.delete(url = 'relationship/' + str(node_id), headers = headers)
		return json.loads(page)

	#get all properties on a relationship
	def get_all_rel_props(self, rel_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'relationship/' + str(rel_id) + '/properties', headers = headers)
		return json.loads(page)

	#set all properties on a relationship
	def set_all_rel_props(self, rel_id, data):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		page = self.post(url = 'relationship/' + str(rel_id) + '/properties', data = data, headers = headers)
		return json.loads(page)

	#get single property of relationship
	def get_rel_prop(self, rel_id, property_name):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'relationship/' + str(rel_id) + '/properties/' + str(property_name), headers = headers)
		return json.loads(page)

	#set single propery of relationship
	def set_rel_prop(self, rel_id, property_name, property_value):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		page = self.post(url = 'relationship/' + str(rel_id) + '/properties/' + str(property_name), data = property_value, headers = headers)
		return json.loads(page)

	#get all relationships
	def get_all_rels(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'node/' + str(node_id) + '/relationships/all', headers = headers)
		return json.loads(page)

	#get incoming relationships
	def get_rel_in(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'node/' + str(node_id) + '/relationships/in', headers = headers)
		return json.loads(page)

	#get outgoing relationships
	def get_rel_out(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'node/' + str(node_id) + '/relationships/out', headers = headers)
		return json.loads(page)

	#get relationships types
	def get_rel_types(self, node_id):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
		}
		page = self.get(url = 'node/' + str(node_id) + '/relationships/types', headers = headers)
		return json.loads(page)
