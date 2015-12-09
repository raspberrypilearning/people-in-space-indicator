# People in Space Indicator

Use the Python requests module to access the *People in Space API* and create an indicator to show the number of people currently in space.

British ESA Astronaut Tim Peake will be going to the International Space Station on 15th December 2015 so this is a great activity to do in time for his arrival. As well as the scientific research Tim will be performing while in space, he's also going to be running experiments using Python code written by school students on two Raspberry Pis as part of the [Astro Pi](https://astro-pi.org) project.

## Browse the People in Space API

**API** stands for *Application Programming Interface*. One form of API is a Web API, which can be used to extract data from a service provided online. Some APIs are open to the public and provide data free of charge. Some APIs require a login to access them, which can be obtained with an application, or can be provided as a service to customers for a fee.

The purpose of providing data via an API is to allow people to access it for their own use, or to build programs with it. Some APIs provide business critical data sets, or otherwise important data about things like the weather financial activity, or even providing access to things like the Twitter stream or Fickr photographs from around the world. Other APIs are just for fun - like the [Pokemon API](http://pokeapi.co/), the [Star Wars API](http://swapi.co/) or the [Adventure Time API](http://adventuretimeapi.com/). While these APIs were made for fun, they can still be used in interesting and useful ways. You could build a Pokemon game in Minecraft, or build a quiz game about the characters in Adventure Time!

You're going to use the *[People in Space API](http://open-notify.org/Open-Notify-API/People-In-Space/)*, maintained and provided for free by [Nathan Bergey](http://open-notify.org/about).

1. Start by opening a web browser and navigating to the following URL:

    ```
    http://api.open-notify.org/astros.json
    ```

1. You should see a white page with some text like so:

    ![People in Space API screenshot](images/people-in-space-api-screenshot.png)

    You are viewing the data provided by the API. This is the manual method of accessing the data.

1. Observe the data provided. It should look something like this:

    ```
    {
      "message": "success",
      "number": 6,
      "people": [
      {
        "craft": "ISS",
        "name": "Mikhail Kornienko"
      },
      ...
    }
    ```

    The format of this data is called **JSON** (pronounced "Jason") which stands for *JavaScript Object Notation*. While the name refers to the programming language *JavaScript*, it's a standard data-interchange format which is made to be portable between languages and applications. If you're familiar with Python's `dictionary` data structure, you'll see the similarities. In other languages a nested array could be used the same way.

1. Observe the following



1. Note that the API provides three pieces of data: `message`, `number` and `people`.

    - `message` is a single string containing the word `success`
    - `number` is the integer value `6`
    - `people` is an array of astronauts

1. Within the `people` array, there are six objects. Each object contains two pieces of data:

    - `craft` is the spacecraft on which the astronaut is present
    - `name` is the astronaut's full name

## Using Python's requests module

Now you'll use the `requests` module in Python to access the API.

1. Open Python 3 from the main menu:

    ![Open Python 3](images/open-python3.png)

1. In the Python shell, type the following line and press **Enter**:

    ```python
    import requests
    ```

    *You're using the Python shell's REPL (Read Evaluative Print Loop) which means each line is executed immediately, rather than writing a file, saving it and running all commands in one go*

1. Now create a variable containing the URL of the API, as a string:

    ```python
    url = "http://api.open-notify.org/astros.json"
    ```

1. Make a request to the API by entering:

    ```python
    r = requests.get(url)
    ```

1. Now simply type `r`, and press **Enter**. This is the same as typing `print(r)` in a file. The REPL allows you to quickly inspect objects this way. You should now see the following:

    ```
    <Response [200]>
    ```

    *This states that `r` contains a `Response` type object, and shows `200`. This is the status code of the request - which means "Success". Other status codes include `404` - which means "File not found" and `500` - "Server error".*

1. Now enter `help(r)`. This shows the docstring (documentation string) for the `Response` object. You should see:

    ```
    Help on Response in module requests.models object:

    class Response(builtins.object)
     |  The :class:`Response <Response>` object, which contains a
     |  server's response to an HTTP request.
     ...
    ```

1. Observe the section of the docstring headed `Data descriptors defined here`. You'll see a list of available properties and their descriptions, including:

    - `apparent_encoding`
    - `content`
    - `is_permanent_redirect`
    - `is_redirect`
    - `links`
    - `ok`
    - `text`

    These properties are essentially variables accessible within an object, For example, `r.ok` is a variable containing the success status of the request (`True` or `False`).

1. Try accessing some of these properties by entering them in the REPL:

    ```python
    >>> r.ok
    True
    >>> r.is_redirect
    False
    >>> r.text
    '{\n  "message": "success", \n  "number": 6...
    ```

    *You'll see that `r.text` seems to contain the data you need. However, this is provided as a string which makes it difficult to use.*

1. Observe the `Methods defined here` part of the docstring, which includes:

    ```
    json(self, **kwargs)
        Returns the json-encoded content of a response, if any.
    ```

    This allows you to access the content of the URL request as JSON, which will make it more useful.

    *A method is a function which belongs to an object, and is accessed the same way as a property but called like a function with `()`, i.e. `r.json()`*

1. Enter `r.json()`. You should see:

    ```
    {'number': 6, 'message': 'success', 'people': [{'craft': 'ISS', 'name': 'Mikhail Kornienko'}, {'craft': 'ISS', 'name': 'Scott Kelly'}, {'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Kimiya Yui'}, {'craft': 'ISS', 'name': 'Kjell Lindgren'}, {'craft': 'ISS', 'name': 'Sergey Volkov'}]}
    ```

1. Save this as a variable:

    ```python
    j = r.json()
    ```

1. Check the data type of the new variable with `type(j)`

    ```python
    >>> type(j)
    <class 'dict'>
    ```

    You'll see that `j` is a dictionary, which is a very useful data structure in Python, essentially identical to the JSON format.

1. To access data inside a dictionary, index it by name with `[]`:

    ```python
    >>> j['number']
    6
    ```

    That's it!

    Looking back and the commands used, putting it all together, the following code was required to retrieve the number of people in space:

    ```python
    import requests

    url = "http://api.open-notify.org/astros.json"

    r = requests.get(url)
    j = r.json()
    n = j['number']
    print(n)
    ```

## What next?

```python
import requests
from time import sleep

url = "http://api.open-notify.org/astros.json"

r = requests.get(url)
j = r.json()
n = j['number']
print(n)
```