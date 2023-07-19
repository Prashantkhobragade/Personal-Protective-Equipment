from fastapi import APIRouter, UploadFile, HTTPException
from service.core.logic.ppe_detection import ppe_detection
import cv2
import shutil
import os

emo_router = APIRouter()

stop_processing = False

@emo_router.post("/detect")
def detect(vid:UploadFile):

    if vid.filename.split(".")[-1] in ("mp4"):
        pass
    else:
        raise HTTPException(
            status_code=415, detail="Not an video"
        )
    
    # Create a temporary file to store the uploaded video
    temp_file_path = f"temp_{vid.filename}"
    with open(temp_file_path, "wb") as temp_file:
        shutil.copyfileobj(vid.file, temp_file)

    # Open the temporary file using VideoCapture
    cap = cv2.VideoCapture(temp_file_path, apiPreference=cv2.CAP_ANY)

    # Perform the detection
    result = ppe_detection(cap)

    # Clean up the temporary file
    cap.release()
    os.remove(temp_file_path)

    return result

@emo_router.get("/stop")
def stop_processing_endpoint():
    global stop_processing
    stop_processing = True
    return {"message": "Processing stopped"}