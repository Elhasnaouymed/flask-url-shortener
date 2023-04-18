# Flask Url Shortener

**flask-url-shortener** Is a flask extension to give the ability of shortening URLs, and supervise them,
completely automatic.

Whether its local URL within your web app, or global URL on the web, you can use **flask-url-shortener** 
to create shorten Link as follows *(simple example)*:

``` python
from flask_url_shortener import Shortener
shortener = Shortener()
...
shortener.init_app(app, db, 'https://your-domin.com', 'rule')
short_link = shortener.shorten('https://www.fsf.org/', _commit=True)
print(short_link.link)
```

in previous example you will get a clickable link like `https://your-domin.com/rule/0f` 
to share with people, when its triggered, will redirect to `http://www.fsf.org/` and of course
will register the click to database automatically,

Keep in mind:
* when creating new shortened URL, you need to manually commit or set `_commit=True`.
* the `init_app` takes your domain name, and also rule of the route you need to use as **clicks listener**.
* the **clicks listener** registered automatically by the extension.
* you can control whether the IP Address and UserAgent of the visitor saved or not, for privacy purposes.
* you can add columns and relationships to Link model or Click model as you wish, and set value to them on the run.
* we are in the process of writing more features, and complete this Documentation.