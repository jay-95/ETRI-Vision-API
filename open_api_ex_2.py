import urllib3
import json
import base64
import cv2
import re


openApiURL = "http://aiopen.etri.re.kr:8000/HumanParsing"
accessKey = "af39439c-23a6-4fdc-8e87-c8b4bb3ae39e"
imageFilePath = "person_detect_1.jpg"
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

#print("[responseCode] " + str(response.status))
#print("[responBody]")
print(response.data)

Im_Person = cv2.imread("person_detect_1.jpg")

#res = response.data.decode('utf-8').replace(r"\\n", "").replace(r"\n", "").replace(r"\t", "").replace("\\", "")

res = response.data.decode('utf-8')
res1 = json.loads(res)
#res1 = re.sub('\s*(\d+)\s+(\d+)', '\\1, \\2', res)
#print(res)
#res2 = json.loads(res)


#res_info = json.loads(res3)
