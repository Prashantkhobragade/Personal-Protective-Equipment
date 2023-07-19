from fastapi import APIRouter, UploadFile, HTTPException

import numpy as np

test_router = APIRouter()


@test_router.get("/test")
def testing():

    

    return {'testing':'testing'}