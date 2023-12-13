import pickle
import sklearn

# Load the model
mhs_model = pickle.load(open('modelnew.sav', 'rb'))

prediction_input = [[5, 5, 5, 6, 6]]
kepuasan = mhs_model.predict(prediction_input)[0]
print(kepuasan)
