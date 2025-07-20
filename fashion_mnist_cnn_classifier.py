import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D, MaxPooling2D, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
X_train = X_train / 255.0
X_test = X_test / 255.0

X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = Sequential([
    Input(shape=(28, 28, 1)),
    BatchNormalization(),
    
    Conv2D(32, kernel_size=3, padding='same', activation='swish'),
    MaxPooling2D(),
    Dropout(0.2),

    Conv2D(64, kernel_size=3, padding='same', activation='swish'),
    MaxPooling2D(),
    Dropout(0.3),

    Conv2D(128, kernel_size=3, padding='same', activation='swish'),
    MaxPooling2D(),
    Dropout(0.4),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),

    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(X_train, y_train,
                    validation_data=(X_test, y_test),
                    batch_size=64,
                    epochs=10,
                    callbacks=[EarlyStopping(patience=3, restore_best_weights=True)])

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.title('Loss')

plt.subplot(1,2,2)
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()
plt.title('Accuracy')

plt.show()

train_loss, train_acc = model.evaluate(X_train, y_train, batch_size=64)
test_loss, test_acc = model.evaluate(X_test, y_test, batch_size=64)
print(f"Train accuracy: {train_acc:.4f}, Test accuracy: {test_acc:.4f}")

y_pred = model.predict(X_test, batch_size=64).argmax(axis=1)

fig, axes = plt.subplots(10, 10, figsize=(12,12))
indices = np.random.choice(len(X_test), 100, replace=False)

for i, ax in enumerate(axes.flat):
    img_idx = indices[i]
    ax.imshow(X_test[img_idx].squeeze(), cmap='gray_r')
    ax.axis('off')
    color = 'green' if y_pred[img_idx] == y_test[img_idx] else 'red'
    ax.set_title(f"True:{class_names[y_test[img_idx]]}\nPred:{class_names[y_pred[img_idx]]}",
                 fontsize=8, color=color)

plt.tight_layout()
plt.show()
