########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

keys = open('keys.py');
key = keys.readline().replace('\n','');

headers = {
    # Request headers
    'api_key': key,
}

params = urllib.parse.urlencode({
    
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    # conn.request("GET", "/TrainPositions/StandardRoutes?contentType={contentType}&%s" % params, "{body}", headers)
    conn.request("GET", "/TrainPositions/StandardRoutes?contentType=json&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################