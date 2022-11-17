import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-1ywbmkoh5znj05ylfvgqq92saysu3c0s9999nr3bwk2k','737d5bcca71833a59364eba9f237a0f2')
service=CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-1ywbmkoh5znj05ylfvgqq92saysu3c0s9999nr3bwk2k:737d5bcca71833a59364eba9f237a0f2@1126bfc5-2dc8-436d-92d7-21d36731aebb-bluemix.cloudantnosqldb.appdomain.cloud')
cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN

while True:
    _,frame=cap.read()
    decodedObjects=pyzbar.decode(frame)
    
    for obj in decodedObjects:
        print("Data",obj.data)
        a=obj.data[8:36]
        cv2.putText(frame,"Ticket",(50,50), font, 2,(255,0,0),3)
        print(a)
        try:
            response=service.get_document(db='qrcode',doc_id=a).get_result()
            print(response)
            time.sleep(5)
        except Exception as e:
            print("Not a valid Ticket")
            time.sleep(5)

    cv2.imshow("Frame",frame)
    if (cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
