
<!DOCTYPE html>
{% load staticfiles %}
<html>
<head>
    <title>Rango</title>
</head>
<body>
    <h1>Rango says...</h1>
    <div>hey there partner!</div>

    <h2>Most Liked Categories</h2>
    
    <div>
    {% if categories %}
    <ul>

        {% for category in categories %}
            <li>
            <a href="/rango/category/{{ category.slug }}">{{ category.name }}</a>
            </li>
        {% endfor %}
    </ul>
    {% else %}
        <strong>There are no categories present.</strong>
    {% endif %}
    </div>

    <h2>Most Viewed Pages</h2>
    <div>
    {% if pages %}
    <ul>
        {% for page in pages %}
        <li>
            <a href= "{{page.url}}">{{page.title}}</a>
        </li>
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
