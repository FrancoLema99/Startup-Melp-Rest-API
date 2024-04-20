from rest_framework import viewsets
from .serializers import RestaurantSerializer
from .models import Restaurant
import pandas as pd
import numpy as np
import json

# Create your views here.


# I import the csv file to be able to do the necessary calculations - Importo el archivo csv para poder hacer los calculos necesarios
df = pd.read_csv('restaurantes.csv') 

# Formula: d = √((x2 - x1)² + (y2 - y1)²)
latitude_center = df['lat'].mean()
longitude_center = df['lng'].mean()
latitude_perimeter = df['lat'].values
longitude_perimeter = df['lng'].values


# Distance between points to calculate the radius - Distancia entre puntos para calcular el radio

distances = np.sqrt((latitude_perimeter - latitude_center)**2 + (longitude_perimeter - longitude_center)**2) # I apply the formula - Aplico la formula
radius = np.max(distances) # Radius - Radio


df['distance'] = np.sqrt((df['lat'] - latitude_center)**2 + (df['lng'] - longitude_center)**2)
restaurants_circle = df[df['distance'] <= radius]

avg_rating = restaurants_circle['rating'].mean() #  Average rating of restaurant inside the circle - Calificación promedio del restaurante dentro del círculo.
std = restaurants_circle['rating'].std() # Standard deviation of rating of restaurants inside the circle - Desviación estándar de la calificación de los restaurantes dentro del círculo


data = {
    'count' : len(restaurants_circle),
    'avg' : avg_rating,
    'std' : std
}


# JSON file - Archivo JSON

with open('restaurants.json', 'w') as file:
    json.dump(data, file, indent=4)

    
class RestaurantViewSet(viewsets.ModelViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
