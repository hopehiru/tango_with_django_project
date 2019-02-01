
{% extends 'rango/base.html' %}
{% load staticfiles %}

{% block title_block %}
    {{ category.name }}
{% endblock %}

{% block body_block %}
<div>
{% if category %}
<h1>{{ category.name }}</h1>
</div>
    {% if pages %}
    <ul>
        {% for page in pages %}
        <li><a href="{{ page.url }}">{{ page.title }}</a></li>
        {% endfor %}
    </ul>
    {% else %}
            <strong>No pages currently in category.</strong>
    {% endif %}

    <a href="{% url 'add_page' category.slug %}">Add a Page</a>
    
    {% else %}
        The specified category does not exist!
    {% endif %}
{% endblock %}

