from pprint import pformat, pprint


def myapplication(environ, start_response):

    environ_formate = pformat(environ)
    corps_bytes = environ_formate.encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain; charset=utf-8')] # Longueur de "Hello World !"]
    
    start_response(status, response_headers)
    
    if environ.get('PATH_INFO') == '/toto':
        return [b'coucou']
    else :
        return [corps_bytes]

#,('Content-Length', str(len(corps_bytes)))