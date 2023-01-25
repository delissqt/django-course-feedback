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