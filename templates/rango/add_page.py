{% extends 'rango/base.html' %}
{% load staticfiles %}
{% block title_block %}
    Add Page
{% endblock %}

{% block body_block %}
<div>
    {% if category %}

<h1>Add a Page to {{category.name}}</h1>

<form id="page_form" method="post" action="/rango/category/{{ category.slug }}/add_page/">

    {% csrf_token %}
    {% for hidden in form.hidden_fields %}
        {{ hidden }}
    {% endfor %}

    {% for field in form.visible_fields %}
        {{ field.errors }}
        {{ field.help_text }}
        {{ field }}
    {% endfor %}

    <input type="submit" name="submit" value="Add Page" />
</form>

    {% else %}
        The specified category does not exist!
    {% endif%}
    </div>	

      

{% endblock %}
