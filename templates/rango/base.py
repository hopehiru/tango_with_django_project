<!DOCTYPE html>
{% load staticfiles %}
{% load rango_template_tags %}

<html>
    <head>
        <title>
        Rango -
        {% block title_block %}
            How to Tango with Django!
        {% endblock %}
        </title>
    </head>
    <body>
        <div>
        
            {% block sidebar_block %}
                {% get_category_list category %}
            {% endblock %}
        </div>
        
        <div>
            {% block body_block %}
            {% endblock %}
        </div>
        <hr />
        

        <div>
            <ul>
            {% if user.is_authenticated %}
                <li><a href="{% url 'restricted' %}">Restricted Page</a></li>
                <li><a href="{% url 'logout' %}">Logout</a></li>
            {% else %}
                <li><a href="{% url 'register' %}">Sign Up</a></li>
                <li><a href="{% url 'login' %}">Login</a><li>
            {% endif %}
                <li><a href="{% url 'add_category' %}">Add New Category</a></li>
                <li><a href="{% url 'about' %}">About</a></li>
                <li><a href="{% url 'index' %}">Index</a></li>
               
            </ul>
        </div>
        
    </body>

</html>
