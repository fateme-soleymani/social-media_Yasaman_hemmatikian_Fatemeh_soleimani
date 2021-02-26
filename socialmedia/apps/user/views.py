from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from apps.user.forms import AddUserForm, LoginForm
from apps.user.models.user import User


# view for user register
class AddUser(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'user/user_form.html', {'form': form})

    def post(self, request):
        """
        save valid data in database(user)
        """
        form = AddUserForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            hash_pass = validated_data['password']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            date_of_birth = validated_data['date_of_birth']
            user_obj = User(user_name=validated_data['email'], first_name=first_name, last_name=last_name,
                            date_of_birth=date_of_birth, hash_pass=hash_pass)
            user_obj.save()
            # return redirect('ok')
        return render(request, 'user/user_form.html', {'form': form})


# view for user login
class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(user_name=form.cleaned_data['user_name'])
            return render(request, 'user/my_profile.html', {'user': user})
        return render(request, 'user/login_form.html', {'form': form})


# view for search for username
class Search(View):
    def get(self, request):
        email = request.GET.get('email')
        if email:
            user = User.objects.filter(user_name__icontains=email)
        else:
            user = None
        return render(request, 'user/search.html', {'user': user})


class UserList(ListView):
    model = User
    context_object_name = 'list_user'


class UserDetail(DetailView):
    model = User
    context_object_name = 'profile_user'
