from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist, BucketlistItem
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


class create (generics.ListCreateAPIView):
    """
    This handles the POST and GET requests
    """

def index(request):
    """
    View page of the home page
    """
    num_bucketlists = Bucketlist.objects.all().count()
    bucketlist_done = BucketlistItem.objects.count()
    template_name = 'rest_api/index.html'
    context = {'num_bucklists' : num_bucketlists, 'bucketlist_done': bucketlist_done}
    return render(request,'rest_api/index.html', context,
    'index.html')



def dashboard(request):
    """
    View page for the dashboard
    """
    template_name = 'rest_api/dashboard.html'

    num_bucketlists = Bucketlist.objects.all().count()
    bucketlist_done = BucketlistItem.objects.done().count()

    return render(request, template_name, context)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            r_pass = form.cleaned_data.get('pasword1')
            user = authenticate(username=username, pasword = r_pass)  
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer




def logout_page(request):
    logout(request)
    return HttpResponseRedirect()