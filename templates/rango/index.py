
<!DOCTYPE html>
{% load staticfiles %}
<html>
<head>
    <title>Rango</title>
</head>
<body>
    <h1>Rango says...</h1>
    <div>hey there partner!</div>

    <div>
    {% if categories %}
    <ul>

        {% for category in categories %}
            <li>{{ category.name }}</li>
        {% endfor %}
    </ul>
    {% else %}
        <strong>There are no categories present.</strong>
    {% endif %}
    </div>

    <div>
        <a href="/rango/about/">About Rango</a><br />
        <img src="{% static "images/rango.jpg" %}" alt="Picture of Rango" />
    </div>
</body>
</html>
