import urllib3
import json
import base64
import cv2

openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "af39439c-23a6-4fdc-8e87-c8b4bb3ae39e"
imageFilePath = "object_detect_airplane.jpg"
im_type = "jpg"
 
file = open(imageFilePath, "rb")
imageContents = base64.b64encode(file.read()).decode("utf8")
file.close()

requestJson = {
    "access_key": accessKey,
    "argument": {
        "type": im_type,
        "file": imageContents
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data)
'''
Im_Airplane = cv2.imread("object_detect_airplane.jpg")
res = response.data.decode('utf-8')
print(type(res))
res_info = json.loads(res)
#print(res_info['return_object'])

clone_air = Im_Airplane.copy()

for data in res_info['return_object']['data']:
   #print("x: %d y: %d w: %d h: %d"  %(data['x'], data['y'], data['width'], data['height']))
   x = int(data['x'])
   y = int(data['y'])
   width = int(data['width'])
   height = int(data['height'])
   cv2.rectangle(clone_air, (x, y), (x+width, y+height), (255, 0, 0), 2)

cv2.imshow('airplanes', clone_air)
cv2.imwrite('airplanes.jpg', clone_air)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''