from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Makeup, Dupe, Photo
from .forms import ReviewsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'catcollec1'

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


def about(request):
  return render(request, 'about.html')

def makeup_index(request):
  makeups = Makeup.objects.all()
  return render(request, 'makeup/index.html', { 'makeups': makeups })

def makeup_detail(request, makeup_id):
  makeup = Makeup.objects.get(id=makeup_id)
  dupes_makeup_doesnt_have = Dupe.objects.exclude(id__in = makeup.dupes.all().values_list('id'))
  reviews_form = ReviewsForm()
  return render(request, 'makeup/detail.html', { 'makeup': makeup, 'reviews_form':reviews_form, 'dupes': dupes_makeup_doesnt_have })

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

def assoc_dupe(request, makeup_id, dupe_id):
  Makeup.objects.get(id=makeup_id).dupes.add(dupe_id)
  return redirect('detail', makeup_id=makeup_id)

def unassoc_dupe(request, makeup_id, dupe_id):
  Makeup.objects.get(id=makeup_id).dupes.remove(dupe_id)
  return redirect('detail', makeup_id=makeup_id)

class DupeList(ListView):
  model = Dupe

class DupeDetail(DetailView):
  model = Dupe

class DupeCreate(CreateView):
  model = Dupe
  fields = '__all__'

class DupeUpdate(UpdateView):
  model = Dupe
  fields = ['name', 'price']

class DupeDelete(DeleteView):
  model = Dupe
  success_url = '/dupes/'

def add_photo(request, makeup_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, makeup_id=makeup_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', makeup_id=makeup_id)



