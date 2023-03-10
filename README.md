# Button Notes

```
<body>
        <form>
            <label for="username">Your name</label>
            <input id="username" name="username" type="text">
            <button>Send</button>
        </form>
    </body>
```

By default button submit the form like `<button type="submit">Send</button>`
If we don't want the button send the data assing in type property a value like `<button type="button">Send</button>`

*The default in many cases especially if we don't configure anything in out HTML code is that a **get** request is sent* by default

That's one of the support that request types we can set.

I get the request simply means I want to get some resource, I want to get some data.
Therefore, if you enter a URL in the address bar of the browser that will always send a get request to the server.


### How change the default mehotd GET by another method

```
<body>
        <form method="POST">
            <label for="username">Your name</label>
            <input id="username" name="username" type="text">
            <button>Send</button>
        </form>
    </body>
```

We want to tell the browser to send a post request instead of a GET request.

To send a **post** request, we got to our form HTML element and add an attribute *method* (`method="POST"`) with that we configure the HTTP method that should be used (remember the default is `method="GET"`)


---

# CSRF

CSRF stands for cross site request forgery.
It's about building requests that look like valid requests, but actually aren't.
Django protects you against with malisious request that is called CSRF token. A token that prevents this attack pattern (manipulate and replace data in the request sent)

## how does it work?

The idea basically, is that in our website and our web application which we're building, we add a dynamically generated token to our generated forms. 
And that token has to be sent to gather with the POST request to our servers. 

If someone thant fakes our site and builds his or her own form, sending fake or manipulated data, that token will be missing because only the official server, our server, our application knows how to build that token and how a valid token should look like because that token is generated on the server.
So therefore, only we are able to build forms that include a valid token and attackers are not.
And on every incoming requests, we can check whether such a valid token is part of the request and we only accept and do something with the data id it is.

# csrf_token

```
<form method="POST">
    {% csrf_token %}
    <label for="username">Your name</label>
    <input id="username" name="username" type="text">
    <button>Send</button>
</form>
```

By adding `{% csrf_token %}` in your Django template, Django will go ahead, generate this unique token and add it in that form.
And then validate that token once your POST request arrives back on the server.

# action property

```
<form action="/" method="POST">
    {% csrf_token %}
    <label for="username">Your name</label>
    <input id="username" name="username" type="text">
    <button>Send</button>
</form>
```

This allows you to specify the path after your domain to which this request should be sent.
If I set it to slash `/` nothing it will be that standard URL, that main domain URL to which it already is being sent.
So you can change that URL to which the request is being sent.
It's still a POST request but now also sent to different URL por example `action="/user-review"`


# Request method POST

```
def review(request): # <--- REQUEST OBJECT
    if request.method == 'POST':
        entered_username = request.POST['username']

    return render(request, "reviews/review.html")
```

`request` object has a method property, which tells us about the HTTP method which was used for this request. 
In our case if it's a GET or a POST request. And we'll get this method identifier as a string.

request.`method` gives us access to the method that was used for submitting tha data.

request.`POST` gives us access to the data itself.
To be precise `POST` will hold a dictionary where the keys are the **names** set on the inputs in the form and the values are the entered values.


So here I can get access to a `username` key on that dictionary, because I have a input named `username` in my form (`name="username"`).
And that will be that entered username.

 ```
 <form action="/" method="POST">
    {% csrf_token %}
    <label for="username">Your name</label>
    <input id="username" name="username" type="text">  # <--- defined here name="username"
    <button>Send</button>
</form>
 ```

---

# Using the Django Form Class

create a file called `forms.py` (this named file is only a common pattern to do so). And we are going to create a *class*. A *class* that defines the shape of our form, the different inputs we want and the validation rules for those inputs.

And we'll then be able to automatically render that form in a template and to automatically let Django validate that form for us.

```
from django import forms

# it's a kinf of a convention that it ends with "Form"
class ReviewForm(forms.Form):
    user_name = forms.CharField()
```

---

# Modelforms

###  Tips

We cant find more information about this topic searching *django class based views* and in the offical django page select *Built-in class-based genereic views*. In here you will see that there actually are a lot of different viws you can extend from 
[link](https://docs.djangoproject.com/en/4.1/topics/class-based-views/)


Models class example:
```
# models.py

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    owner_comment = models.TextField() # only for example
```

Adding items in Class Model Based Form, we can added in the list the items we wan display in the form
```
# forms.py

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["user_name", "review_text", "rating"]
```

If we want add all items of the model we can do the next
```
# forms.py

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
```

Alternatively, if you know that you wanna render all fields except one maybe, you could set the `exclude` field and the list all the fields that should be excluded

```
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["owner_commet"]


---

# Template View

TemplateView it's specifically focused on allowing you to build view classes that render templates.

```
# views.py
# example usign TemplateView

from django.views.generic.base import TemplateView

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context

    # the idea here is taht in this get_context_data method you should return the context that is exposed to the
    # template
```

We can use this imported template view and inherit that instead of just view. When doing that you don't define a get method here anymore. Instead, inthat case here, we??re focused on returning a template. That's why we use this template view.

```
# views.py
# example using View

```
from django.views import View

class ThankyouView(View):

    def get(self, request)
        return render(request, "reviews/thank_you.html") 
```

---

# ListView


```
from django.views.generic import ListView
```

`ListView` is a more specialized template view. It's still all about rendering a template for a get request but it then also specifically for **fetching a list of data*based on some model*.

```
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"

    # def get_context_data 
    # def get_ordering 
```
| function | description |
|----------|-------------|
|`def get_context_data`| We can override context_data if we need to pass additional context to the template. |
|`def get_ordering`| We can override get_ordering to control how the fetched data should be ordered. |
|`def get_queryset`| We can override get_queryset which allows us to change how the data is fetched, for example If you want to get a filtered list or anything like this. |


When we use Listview, Django will fecth all those reviews (objects) but it will expose them in my template as `object_list`


```
#views.py
from django.views.generic import ListView
from .models import Review

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # get the data as object_list
```

 reviews_list.html
```
{% extends "reviews/base.html" %}


{% block title %}All reviews{% endblock %}

{% block content %}
    <ul>
        {% for review in object_list %}
            <li>
                {{ review.user_name }} - Rating: {{ review.rating }}
            </li>
        {% endfor %}
    </ul>

{% endblock %}
```

Is possible to configure how this list you works. For exmaple We can change *objects_list* is named by another one word.
You can add a context_object_name property which allows you to define the name of the data which you will have when it's exposed yo your template.
So if I set this to reviews here, I can use that fetch list of data under the name reviews in the template.

views.py
```
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
```

 review_list.html
```
{% extends "reviews/base.html" %}


{% block title %}All reviews{% endblock %}

{% block content %}
    <ul>
        {% for review in reviews %}
            <li>
                {{ review.user_name }} - Rating: {{ review.rating }}
            </li>
        {% endfor %}
    </ul>

{% endblock %}
```

We can filtering data for fetching it to the template

```
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
```

---

# DetailView

django takes automatically model name and anc hange to lower case, for expose in template, but also wroks with *object* word
views.py
```
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    # 
```

imporant change the url by <pk>
urls.py
```
from django.urls import path
from . import views


urlpatterns = [
    ...
    path("reviews/<int:pk>", views.ReviewDetailView.as_view()),
]
```

review_detail.html
```
{% extends "reviews/review.html" %}


{% block title %}Review Detail{% endblock %}

{% block content %}

    <h2>{{ object.user_name }}</h2>
    <p>Rating: {{ review.rating }}</p>
    <p>{{ review.review_text }}</p>

{% endblock %}
```

---
 # FormView

 without use FormView

 ```
 class ReviewView(View):

    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
        "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
        "form": form
        })
 ```

 usign 

 ```
 class ReviewView(FormView):
    # tell what form should use
    form_class = ReviewForm
    template_name = "reviews/review.html"

    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
 ```

 ---

 # CreateView

with CreateView
 ```
 class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm # fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"
 ```

 without CreateView

```
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"

    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

```

---
 # TemplateView

with TemplateView

```
class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context
```

without TemplateView

```
def thank_you(request):
    return render(request, "reviews/thank_you.html")
```

---

# Using Models for File Storage

In this models, `FileField` wants a file, but the interesting thing now is that this file will not be stored in a database because  **it is considered a bad practice to store files in the database** It bloats the database, makes it slow, and the database, makes it slow. The database simply is no file storage. Instead files shuld be stored on hard drives.

```
# models.py

class UserProfile(models.Model):
    image = models.FileField(upload_to="data")
```
`FileField` will do under the hood once we save a Model with a file, it is will take that file and move it somewhere on our hard drive, on our disc and only dtore the path to that file in the Model in the database.

So, will tell Django where our files should be stored. 

```
settings.py


MEDIA_ROOT = BASE_DIR / "uploads"
```


After saved a image we can see the path storage in the data base , inside python shell

```
from profiles.models import UserProfile
UserProfile.objects.all()

$ <QuerySet [<UserProfile: UserProfile object (1)>, <UserProfile: UserProfile object (2)>]>

UserProfile.objects.all()[0].image.path

$ 'C:\\Users\\Forest\\Desktop\\Proyectos\\ProyectosInternos\\django-course-feedback\\feedback\\uploads\\data\\leaf_kCbSH1X.jpg'
```

---

#Imagefield

In order to user Imagefiled is necessary install `Pyllow`

```
# models.py
class UserProfile(models.Model):
    image = models.ImageField(upload_to="data")
```

```
# forms.py
class ProfileForm(forms.Form):
    user_image = forms.ImageField()
```

---

# CreateView

using `CreateView`

```
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
```


**without** using `CreateView`
```
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    
    def post(self, request):
        #request.FILES["image"]
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            #store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })

```

---

# Session

|Session|
|-------|
|A "ongoing connection" between a client (browser) and server|
|Data stored in a session presists as long as the sessions is active|

```
 _________________                                                 _____________________
|           ______|________                             ___________|______             |
|          | Cookie with  |                             | Session data + |             |
|  Client  | Session ID   |  <----------------------->  | identifier     |   Server    |
|          |______________|                             |________________|             | 
|_________________|                                            |    |__________________|
                                                               |
                                                               \/
                                                ____________________________
                                                | Stored in sesson storage, |
                                                | typically a DB            |
                                                |___________________________|

```

A session is a long-term relation between client and server, but it can be cleared and deleted and reset.
It??s not forever, but it is long living and we as a developer will be able to decide how long it will live.

Sessions are about storing data and information