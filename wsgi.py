from wsgiref import simple_server

def application(environ, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    doc = """
<html>
    <body>  
        <form action="http://153.120.169.167:8081" method="get">
        <div>
            <label for="say">What greeting do you want to say?</label>
            <input name="say" id="say" value="Hi">
        </div>
        <div>
            <label for="to">Who do you want to say it to?</label>
            <input name="to" id="to" value="Mom">
        </div>
        <div>
            <button>Send my greetings</button>
        </div>
    </body>
</html>
"""
    return doc

if __name__ == '__main__':
    server = simple_server.make_server('', 8081, application)
    server.serve_forever()
