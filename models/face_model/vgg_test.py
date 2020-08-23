# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:24:40 2020

@author: sodaus
"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
# from PIL import Image


datagen = ImageDataGenerator(
    validation_split=0.2,
    rescale=1./255,
    data_format='channels_first'
)

data_dir = r'/Users/sodaus/Desktop/data/ver3/tmp'
train_generator = datagen.flow_from_directory(
    directory=data_dir,
    subset='training',
    target_size=(224, 224),
    batch_size=32,
    shuffle=True,
    class_mode='binary',
    seed=112
)

valid_generator = datagen.flow_from_directory(
    directory=data_dir,
    subset='validation',
    target_size=(224, 224),
    batch_size=32,
    shuffle=True,
    class_mode='binary',
    seed=112
)



#train_data[0][0].shape



def vgg_face(weights_path=None):
    img = Input(shape=(3, 224, 224))

    pad1_1 = ZeroPadding2D(padding=(1, 1), data_format='channels_first')(img)
    conv1_1 = Convolution2D(64, (3, 3), activation='relu', name='conv1_1', data_format='channels_first')(pad1_1)
    pad1_2 = ZeroPadding2D(padding=(1, 1), data_format='channels_first')(conv1_1)
    conv1_2 = Convolution2D(64, (3, 3), activation='relu', name='conv1_2', data_format='channels_first')(pad1_2)
    pool1 = MaxPooling2D((2, 2), strides=(2, 2), data_format='channels_first')(conv1_2)

    pad2_1 = ZeroPadding2D((1, 1), data_format='channels_first')(pool1)
    conv2_1 = Convolution2D(128, (3, 3), activation='relu', name='conv2_1', data_format='channels_first')(pad2_1)
    pad2_2 = ZeroPadding2D((1, 1), data_format='channels_first')(conv2_1)
    conv2_2 = Convolution2D(128, (3, 3), activation='relu', name='conv2_2', data_format='channels_first')(pad2_2)
    pool2 = MaxPooling2D((2, 2), strides=(2, 2), data_format='channels_first')(conv2_2)

    pad3_1 = ZeroPadding2D((1, 1), data_format='channels_first')(pool2)
    conv3_1 = Convolution2D(256, (3, 3), activation='relu', name='conv3_1', data_format='channels_first')(pad3_1)
    pad3_2 = ZeroPadding2D((1, 1), data_format='channels_first')(conv3_1)
    conv3_2 = Convolution2D(256, (3, 3), activation='relu', name='conv3_2', data_format='channels_first')(pad3_2)
    pad3_3 = ZeroPadding2D((1, 1), data_format='channels_first')(conv3_2)
    conv3_3 = Convolution2D(256, (3, 3), activation='relu', name='conv3_3', data_format='channels_first')(pad3_3)
    pool3 = MaxPooling2D((2, 2), strides=(2, 2), data_format='channels_first')(conv3_3)

    pad4_1 = ZeroPadding2D((1, 1), data_format='channels_first')(pool3)
    conv4_1 = Convolution2D(512, (3, 3), activation='relu', name='conv4_1', data_format='channels_first')(pad4_1)
    pad4_2 = ZeroPadding2D((1, 1), data_format='channels_first')(conv4_1)
    conv4_2 = Convolution2D(512, (3, 3), activation='relu', name='conv4_2', data_format='channels_first')(pad4_2)
    pad4_3 = ZeroPadding2D((1, 1), data_format='channels_first')(conv4_2)
    conv4_3 = Convolution2D(512, (3, 3), activation='relu', name='conv4_3', data_format='channels_first')(pad4_3)
    pool4 = MaxPooling2D((2, 2), strides=(2, 2), data_format='channels_first')(conv4_3)

    pad5_1 = ZeroPadding2D((1, 1), data_format='channels_first')(pool4)
    conv5_1 = Convolution2D(512, (3, 3), activation='relu', name='conv5_1', data_format='channels_first')(pad5_1)
    pad5_2 = ZeroPadding2D((1, 1), data_format='channels_first')(conv5_1)
    conv5_2 = Convolution2D(512, (3, 3), activation='relu', name='conv5_2', data_format='channels_first')(pad5_2)
    pad5_3 = ZeroPadding2D((1, 1), data_format='channels_first')(conv5_2)
    conv5_3 = Convolution2D(512, (3, 3), activation='relu', name='conv5_3', data_format='channels_first')(pad5_3)
    pool5 = MaxPooling2D((2, 2), strides=(2, 2), data_format='channels_first')(conv5_3)

    flat = Flatten(data_format='channels_first')(pool5)
    fc6 = Dense(4096, activation='relu', name='fc6')(flat)
    fc6_drop = Dropout(0.5)(fc6)
    fc7 = Dense(4096, activation='relu', name='fc7')(fc6_drop)
    fc7_drop = Dropout(0.5)(fc7)
    out = Dense(2622, activation='softmax', name='fc8')(fc7_drop)

    model = Model(inputs=img, outputs=out)

    if weights_path:
        model.load_weights(weights_path)

    return model



# if __name__ == "__main__":
#     im = Image.open('A.J._Buckley.jpg')
#     im = im.resize((224,224))
#     im = np.array(im).astype(np.float32)
# #    im[:,:,0] -= 129.1863
# #    im[:,:,1] -= 104.7624
# #    im[:,:,2] -= 93.5940
#     im = im.transpose((2,0,1))
#     im = np.expand_dims(im, axis=0)

#     # Test pretrained model
#     model = vgg_face('vgg-face-keras.h5')
#     out = model.predict(im)
#     print(out[0][0])1
vgg_face().summary()

base_model = vgg_face(r'C:\Users\sodaus\Desktop\data\vgg-face-keras-fc.h5')

# exclude fc layers
Global_Avg_Pool = tf.keras.layers.GlobalAveragePooling2D(data_format='channels_first')(base_model.layers[-7].output)

# add our own fc layers
fc6 = Dense(32, activation='relu', name='fc6')(Global_Avg_Pool)  # 4096
fc6_drop = Dropout(0.5)(fc6)
fc7 = Dense(16, activation='relu', name='fc7')(fc6_drop)  # 4096
fc7_drop = Dropout(0.5)(fc7)
out = Dense(1, activation='sigmoid', name='fc8')(fc7_drop)

my_model = Model(inputs=base_model.input, outputs=out)

# freeze pretrained weights(layers) and train our own fc layers
for layer in my_model.layers:
  if 'fc' in layer.name:
    layer.trainable = True
  else:
    layer.trainable = False

my_model.summary()

my_model.compile(optimizer='adam',
                #  loss=tf.losses.SparseCategoricalCrossentropy(),
                 loss=tf.losses.BinaryCrossentropy(),
                 metrics=['accuracy'])



# cb_early_stopper = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
with tf.device('/device:GPU:0'):
    fit_history = my_model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=5,
        validation_data=valid_generator,
        validation_steps=len(valid_generator)
        # callbacks=[cb_early_stopper]
    )

#성능평가
# model.evaluate([face_pic_test, head_pose_test],[y_test])


# history plot
import matplotlib.pyplot as plt
plt.plot(fit_history.history["accuracy"])
plt.plot(fit_history.history['val_accuracy'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy","Validation Accuracy \n"])
plt.show()

# plt.plot(fit_history.history["loss"])
# plt.plot(fit_history.history['val_loss'])
# plot_model(model, 'model_test_01.png')