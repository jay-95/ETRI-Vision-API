import urllib3
import json
import os
import cv2

openApiURL = "http://aiopen.etri.re.kr:8000/VideoParse"
accessKey = "af39439c-23a6-4fdc-8e87-c8b4bb3ae39e"
videoFilePath = "demo-3.mp4"

file = open(videoFilePath,'rb')
fileContent = file.read()
file.close();

requestJson = {
	"access_key": accessKey,
	"argument": {}
}

http = urllib3.PoolManager()
response = http.request(
	"POST",
	openApiURL,
	fields={
		'json': json.dumps(requestJson),
		'uploadfile': (os.path.basename(file.name), fileContent)
	}
)

#print("[responseCode] " + str(response.status))
#print("[responBody]")
#print(response.data)

res_info = json.loads(response.data.decode('utf-8'))

f_id = res_info['return_object']['file_id']

capture = cv2.VideoCapture("demo-3.mp4")

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("demo-3.mp4.mp4")
        
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break
 
capture.release()
cv2.destroyAllWindows()