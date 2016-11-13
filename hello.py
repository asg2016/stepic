#! usr/bin/python
#-*- coding utf-8 -*-

def server(environ, start_response):
  data=''
  for line in environ['QUERY_STRING'].split('&'):
    data = data + line + '\n'
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [data]
