{% extends 'rango/base.html' %}
{% load staticfiles %}

{% block title_block %}
    {{ category.name }}
{% endblock %}

{% block body_block %}
    Since you're logged in, you can see this text!
{% endblock %}
