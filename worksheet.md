# People in Space Indicator

Use the Python requests module to access the *People in Space API* and create an indicator to show the number of people currently in space.

British ESA Astronaut Tim Peake will be going to the International Space Station on 15th December 2015 so this is a great activity to do in time for his arrival. As well as the scientific research Tim will be performing while in space

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

    The

1. Within the `people` array, there are six objects

## Using Python's requests module

Now you'll use the `requests` module in Python

1. Open Python 3 from the main menu:

    ![](images/open-python3.png)



## What next?
