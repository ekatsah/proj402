<p style="border: 1px white solid; padding: 5px;">
  <strong>On {{ object.date|date:"d/m/y H:i" }}, {{ object.owner.username }} wrote :</strong><br>
{{ object.text }}</p>

<form method="post" action="{% url post_msg %}" id="new_msg_form">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table><br>
    <center>
      <input type="submit" value="send" id="send" 
          onclick="return Pload('new_msg_form', '{% url post_msg %}', function() {Iload('{% url view_thread object.thread.id %}');});"/>
    </center>
    <script type="text/javascript">
    $("#id_thread").val({{ object.thread.id }});
    $("#id_reference").val({{ object.id }});
    </script>
</form>

