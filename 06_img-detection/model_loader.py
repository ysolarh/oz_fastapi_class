import tensorflow as tf


def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print("***Success Model Loaded***")
    return model


model = load_model()
