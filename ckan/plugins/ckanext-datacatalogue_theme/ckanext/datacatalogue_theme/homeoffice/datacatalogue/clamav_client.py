

class ClamAVClient:
    def scanFile(fileLocation):
        if(True):
            h4 = http.client.HTTPConnection('localhost', 8765, timeout=10)
        else:
            h4 = http.client.HTTPSConnection('localhost', 8765, timeout=10)
        fileObj = open(filename)
        
        h4.request("POST", "/scan", body=fileObj)
        response = h4.getResponse()
        print(response.status, response.reason)
        data = response.read()
        print(data)

        return False

file_location = sys.argv[1]

service = ckanapi.RemoteCKAN()
print(service.scanFile(file_location))
