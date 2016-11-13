#! usr/bin/python
#-*- coding utf-8 -*-

from urlparse import parse_qs
def wsgi_application(environ, start_response):
	start_response('200 OK', headers, [('Content-Type', 'text/plain')])
	qs = parse_qs(environ['QUERY_STRING'])
	return [  ]

from urlparse import parse_qs                                                                                   
def application(environ, start_response):                                                                         
    start_response('200 OK', [('Content-Type',' text/plain')])                                                  
    qs = parse_qs(environ['QUERY_STRING'])                                                                      
    return['%s=%s<br />' % (k, qs[k][0]) for k in qs]


def app (environ, start_response):
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [item+"\r\n" for item in resp]
  return resp
  
def application(environ, start_response):                                                                                                          
	start_response('200 OK', [('Content-Type','text/plain')])                                                                                      
	qstring = environ['QUERY_STRING'].split("&")                                                                                                   
	result = [item+"\r\n" for item in qstring]                                                                                                     
	return result
