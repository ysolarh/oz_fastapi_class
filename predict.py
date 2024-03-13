import numpy as np
from PIL import Image
# from keras.src.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.imagenet_utils import decode_predictions

from model_loader import model


# 이미지를 예측해서 결과를 알려주는 함수
def predict(img: Image):
    image = np.asarray(img.resize((224, 224)))[..., :3]  # RGB
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0  # -1 ~ 1 사이의 숫자로 바뀜 - MinMax Scaler(정규화)
    result = decode_predictions(model.predict(image), 2)[0]
    result_list = []
    for res in result:
        print(res)
        result_list.append({"class": res[1], "predictions": f"{res[2]*100:0.2f} %"})
        return result_list
