from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Makeup, Dupe, Photo
from .forms import ReviewsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'catcollec1'

class MakeupCreate(LoginRequiredMixin,CreateView):
  model = Makeup
  fields = '__all__'

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class MakeupUpdate(LoginRequiredMixin,UpdateView):
  model = Makeup
  fields = '__all__'

class MakeupDelete(LoginRequiredMixin,DeleteView):
  model = Makeup
  success_url = '/makeup/'

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def makeup_index(request):
  makeups = Makeup.objects.filter(user=request.user)
  return render(request, 'makeup/index.html', { 'makeups': makeups })

@login_required
def makeup_detail(request, makeup_id):
  makeup = Makeup.objects.get(id=makeup_id)
  dupes_makeup_doesnt_have = Dupe.objects.exclude(id__in = makeup.dupes.all().values_list('id'))
  reviews_form = ReviewsForm()
  return render(request, 'makeup/detail.html', { 'makeup': makeup, 'reviews_form':reviews_form, 'dupes': dupes_makeup_doesnt_have })

@login_required
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

@login_required
def assoc_dupe(request, makeup_id, dupe_id):
  Makeup.objects.get(id=makeup_id).dupes.add(dupe_id)
  return redirect('detail', makeup_id=makeup_id)

@login_required
def unassoc_dupe(request, makeup_id, dupe_id):
  Makeup.objects.get(id=makeup_id).dupes.remove(dupe_id)
  return redirect('detail', makeup_id=makeup_id)

class DupeList(LoginRequiredMixin,ListView):
  model = Dupe

class DupeDetail(LoginRequiredMixin,DetailView):
  model = Dupe

class DupeCreate(LoginRequiredMixin,CreateView):
  model = Dupe
  fields = '__all__'

class DupeUpdate(LoginRequiredMixin,UpdateView):
  model = Dupe
  fields = ['name', 'price']

class DupeDelete(LoginRequiredMixin,DeleteView):
  model = Dupe
  success_url = '/dupes/'

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



