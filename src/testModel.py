from train import test_data, siamese_model
from tensorflow.keras.metrics import Precision, Recall

test_input, test_val, y_true = test_data.as_numpy_iterator().next()
y_hat = siamese_model.predict([test_input, test_val]) 
y_hat = [1 if prediction > 0.5 else 0 for prediction in y_hat]

print(y_hat)
print(y_true)

m = Recall()
m.update_state(y_true, y_hat)
m.result().numpy()
