from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Makeup

# class Makeup:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, category, description, price):
#     self.name = name
#     self.category = category
#     self.description = description
#     self.price = price

# makeups = [
#   Makeup('High Gloss', 'Lipstick', 'High Shine Gloss is an ultra-glossy, luminous gloss that glides on the lips smoothly and evenly with added shea butter leaving behind a radiant and moisturizing shine.', 16),
#   Makeup('Sunset Eyeshadow Palette', 'EyeShadow', 'An eyeshadow palette with 15 shades in Natasha Denonas signature matte, duo chrome, metallic, and chroma crystal finishes.', 170),
#   Makeup('Matte Lipstick', 'Lipstick', 'A creamy rich lipstick formula with high colour payoff in a no-shine matte finish.', 24)
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return HttpResponse('<h1>About the MakeupCollector</h1>')

def about(request):
  return render(request, 'about.html')

def makeup_index(request):
  makeups = Makeup.objects.all()
  return render(request, 'makeup/index.html', { 'makeups': makeups })

def makeup_detail(request, makeup_id):
  makeup = Makeup.objects.get(id=makeup_id)
  return render(request, 'makeup/detail.html', { 'makeup': makeup })
