from io import BytesIO

from fastapi import FastAPI, UploadFile, File
from PIL import Image

from predict import predict

app = FastAPI()


@app.post('/predict/image')
async def predict_image(file: UploadFile = File(...)):
    # 예외처리
    extension = file.filename.split(".")[-1] in ('jpg', 'png', 'jpeg')

    if not extension:
        return "Change the extension"

    img = Image.open(BytesIO(await file.read()))
    print('img type:', img)

    result = predict(img)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app")
