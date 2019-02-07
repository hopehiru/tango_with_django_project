{% extends 'rango/base.html' %}
{% load staticfiles %}

{% block title_block %}
    Register
{% endblock %}

{% block body_block %}
    <h1>Register for Rango</h1>
    {% if registered %}
        Rango says: <strong>thank you for registering!</strong>
        <a href="{% url 'index' %}">Return to the homepage.</a><br />
    {% else %}
        Rango says: <strong>register here!</strong><br />        
        <form id="user_form" method="post" action="{% url 'register' %}" enctype="multipart/form-data">
        
        <!-- Display each form --> 
        {% csrf_token %}
        {{ user_form.as_p }}
        {{ profile_form.as_p }}
        
         <!-- Provide a button to click to submit the form. -->         
        <input type="submit" name="submit" value="Register" />
    </form>
    {% endif %}
{% endblock %}
