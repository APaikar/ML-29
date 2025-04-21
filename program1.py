import pickle

with open('linear (1).pkl','rb') as file:
    model = pickle.load(file)

values = [[9,128,90,2]]
result = model.predict(values)
print(result[0])