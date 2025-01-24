import os
from paddleocr import PaddleOCR
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

ocr = PaddleOCR(use_angle_cls=True, lang='hi')

# Pydantic model to validate the input request
class FilePathRequest(BaseModel):
    file_path: str

@app.post("/ocr")
async def process_image(request: FilePathRequest):
    try:
        # file_path = request.file_path

        # if not file_path:
        #     raise HTTPException(status_code=400, detail="File path is required")

        # # Adjust the path to point to the mounted volume
        # container_file_path = os.path.join("/app/photos", os.path.basename(file_path))

        # if not os.path.exists(container_file_path):
        #     raise HTTPException(status_code=400, detail=f"File does not exist: {container_file_path}")

        # concatenated_text = ""
        # result = ocr.ocr(container_file_path, cls=True)
        # if result[0] is not None:
        #     concatenated_text = " ".join([line[1][0] for line in result[0]])

        # # time.sleep(110)
        # return {"concatenated_text": concatenated_text}

        count = 0;
        while count <=50:
            file_path = request.file_path

            if not file_path:
                raise HTTPException(status_code=400, detail="File path is required")

            # Adjust the path to point to the mounted volume
            container_file_path = os.path.join("/app/photos", os.path.basename(file_path))

            if not os.path.exists(container_file_path):
                raise HTTPException(status_code=400, detail=f"File does not exist: {container_file_path}")

            concatenated_text = ""
            result = ocr.ocr(container_file_path, cls=True)
            if result[0] is not None:
                concatenated_text = " ".join([line[1][0] for line in result[0]])
            count +=1;

        return {"concatenated_text": concatenated_text}
        
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
