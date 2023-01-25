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

## how does ir work?

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