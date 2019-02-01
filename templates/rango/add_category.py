{% extends 'rango/base.html' %}
{% load staticfiles %}
{% block title_block %}
		Add Category
{% endblock %}
    {% block body_block %}
	<div>
            <h1>Add a Category</h1>
	    <form role="form" id="category_form" method="post" action="{% url 'add_category' %}">
	    {% csrf_token %}
	    {% for hidden in form.hidden_fields %}
                {{ hidden }}
            {% endfor %}
            {% for field in form.visible_fields %}
                {{ field.errors }}
                {{ field.help_text }}
                {{ field }}
            {% endfor %}
             <input type="submit" name="submit" value="Create Category" /><br/>
             </form>
        </div>	

{% endblock %}




