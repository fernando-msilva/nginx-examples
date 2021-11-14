import os 

def application(env,start_response):
    start_response('200 ok',[('Content-Type','application/json')])
    return [str({'container_id':os.environ['HOSTNAME']}).encode()]