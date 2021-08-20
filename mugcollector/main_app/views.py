from django.shortcuts import render, redirect
from .models import Mug, Coaster
from .forms import TeatimeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import HttpResponse

# Create your views here.

# Define the home view
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def mugs_index(request):
    mugs = Mug.objects.filter(user=request.user)
    return render(request, "mugs/index.html", {"mugs": mugs})


@login_required
def mugs_detail(request, mug_id):
    mug = Mug.objects.get(id=mug_id)
    coasters_mug_doesnt_have = Coaster.objects.exclude(
        id__in=mug.coasters.all().values_list("id")
    )
    teatime_form = TeatimeForm()
    return render(
        request,
        "mugs/detail.html",
        {
            "mug": mug,
            "teatime_form": teatime_form,
            "coasters": coasters_mug_doesnt_have,
        },
    )


@login_required
def add_teatime(request, mug_id):
    form = TeatimeForm(request.POST)
    if form.is_valid():
        new_teatime = form.save(commit=False)
        new_teatime.mug_id = mug_id
        new_teatime.save()
    return redirect("detail", mug_id=mug_id)


class MugCreate(CreateView):
    model = Mug
    fields = ["name", "color", "description", "age"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MugUpdate(LoginRequiredMixin, UpdateView):
    model = Mug
    fields = ["color", "description", "age"]


class MugDelete(LoginRequiredMixin, DeleteView):
    model = Mug
    success_url = "/mugs/"


class CoasterList(LoginRequiredMixin, ListView):
    model = Coaster


class CoasterDetail(LoginRequiredMixin, DetailView):
    model = Coaster


class CoasterCreate(LoginRequiredMixin, CreateView):
    model = Coaster
    fields = "__all__"


class CoasterUpdate(LoginRequiredMixin, UpdateView):
    model = Coaster
    fields = ["name", "color"]


class CoasterDelete(LoginRequiredMixin, DeleteView):
    model = Coaster
    success_url = "/coasters/"


@login_required
def assoc_coaster(request, mug_id, coaster_id):
    Mug.objects.get(id=mug_id).coasters.add(coaster_id)
    return redirect("detail", mug_id=mug_id)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
