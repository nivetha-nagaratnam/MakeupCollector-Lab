from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Makeup
from .forms import ReviewsForm

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

class MakeupCreate(CreateView):
  model = Makeup
  fields = '__all__'

class MakeupUpdate(UpdateView):
  model = Makeup
  fields = '__all__'

class MakeupDelete(DeleteView):
  model = Makeup
  success_url = '/makeup/'

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

# def about(request):
#   return HttpResponse('<h1>About the MakeupCollector</h1>')

def about(request):
  return render(request, 'about.html')

def makeup_index(request):
  makeups = Makeup.objects.all()
  return render(request, 'makeup/index.html', { 'makeups': makeups })

def makeup_detail(request, makeup_id):
  makeup = Makeup.objects.get(id=makeup_id)
  reviews_form = ReviewsForm()
  return render(request, 'makeup/detail.html', { 'makeup': makeup, 'reviews_form':reviews_form })

def add_review(request, makeup_id):
  form = ReviewsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_review = form.save(commit=False)
    new_review.makeup_id = makeup_id
    new_review.save()
  return redirect('detail', makeup_id=makeup_id)
