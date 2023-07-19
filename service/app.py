from fastapi import APIRouter, File, UploadFile, FastAPI
from service.Api.api import main_router
from fastapi.responses import FileResponse
from ultralytics import YOLO
import cv2
import cvzone
import numpy as np
import math

app = FastAPI(project_name = "PPE Object Detaction")
app.include_router(main_router)




@app.get("/")
def root():
    return {"PPE": "Detection"}

    