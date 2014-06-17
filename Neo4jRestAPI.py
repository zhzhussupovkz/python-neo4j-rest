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

	def cypher_query(self, query, params):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"Content-Type" : "application/json",
		}
		data = {
			"query" : query,
			"params" : params,
		}
		page = self.post('cypher', data = data, headers = headers)
		return json.loads(page)

	def streaming(self):
		headers = {
			"Accept" : "application/json; charset=UTF-8",
			"X-Stream" : "true",
		}
		page = self.get(url = '', headers = headers)
		return json.loads(page)

