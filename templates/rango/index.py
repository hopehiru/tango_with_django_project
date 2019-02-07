{% extends 'rango/base.html' %}
{% load staticfiles %}
{% block title_block %}
    Index
{% endblock %}
{% block body_block %}
    <div>
<h1>Rango says...</h1>

    {% if user.is_authenticated %}
        howdy {{ user.username }}!
    {% else %}
        hey there partner!
    {% endif %}

    </div>
    <div>
        <div>
            <h3>Most Liked Categories</h3>	
        </div>

    {% if categories %}
    <ul>
        {% for category in categories %}
            <li><a href="{% url 'show_category' category.slug %}">{{ category.name }}</a></li>
        {% endfor %}
    </ul>

{% else %}
    <strong>There are no categories present.</strong>
{% endif %}

    </div>
        <div>
            <div>
                <h3>Most Viewed Pages</h3>
            </div>

	{% if pages %}
        <ul>
            {% for page in pages %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
            {% endfor %}
        </ul>
        
{% else %}
    <strong>There are no categories present.</strong>
{% endif %}
</div>

<img src="{% static "images/rango.jpg" %}" alt="Picture of Rango" /> 
{% endblock %}
