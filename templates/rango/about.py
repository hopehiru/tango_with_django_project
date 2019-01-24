<!DOCTYPE html>

{% load staticfiles %} <!-- New line -->
<html>
    <head>
        <title>Rango</title>
    </head>
    <body>
        <h1>Rango says...</h1>
        <div>
            Hello <br />
            
            <strong>{{ boldmessage }}</strong><br />
        </div>
        <div>
            <a href="/rango/index/">Index</a><br /> <img src="{% static "images/rango.jpg" %}" alt="Picture of Rango" /> <!-- New line -->
        </div>
        <div>
            This tutorial has been put together by Hope
        </div>
    </body>
</html>
