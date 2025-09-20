<!-- Example form in form_example.html -->
<form method="post" action="{% url 'your_view_name' %}">
    {% csrf_token %}
    <!-- Your form fields here -->
    <button type="submit">Submit</button>
</form>
