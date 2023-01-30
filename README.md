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
        fields = '__all__'
```

Alternatively, if you know that you wanna render all fields except one maybe, you could set the `exclude` field and the list all the fields that should be excluded

```
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["owner_commet"]
