#trains and tests our ai 

from train import test_data, siamese_model
from tensorflow.keras.metrics import Precision, Recall
from matplotlib import pyplot as plt

print(len(test_data))
test_input, test_val, y_true = test_data.as_numpy_iterator().next()
print(len(test_input))
y_hat = siamese_model.predict([test_input, test_val]) 
y_hat = [1 if prediction > 0.5 else 0 for prediction in y_hat]

print(y_hat)
print(y_true)

rec_m = Recall()
rec_m.update_state(y_true, y_hat)
print(rec_m.result().numpy())

rec_p = Precision()
rec_m.update_state(y_true, y_hat)
print(rec_m.result().numpy())

plt.figure(figsize=(18,8))
plt.subplot(1, 2, 1)
plt.imshow(test_input[0])
plt.subplot(1, 2, 2)
plt.imshow(test_val[0])
