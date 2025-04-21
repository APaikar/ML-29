from django.shortcuts import render
import pickle
import os


def predict(request):
    prediction = None

    if request.method == 'POST':
        try:
            # Load the model
            model_path = os.path.join(os.path.dirname(__file__), 'linear (1).pkl')
            with open(model_path, 'rb') as f:
                model = pickle.load(f)

            # Get user inputs with validation
            brand = int(request.POST.get('brand'))
            memory = int(request.POST.get('memory'))
            refresh = int(request.POST.get('refresh'))
            cameras = int(request.POST.get('cameras'))

            # Make prediction
            values = [[brand, memory, refresh, cameras]]
            prediction = round(model.predict(values)[0], 2)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'core/predict.html', {'prediction': prediction})