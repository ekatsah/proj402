<form method="post" action="" id="new_thread_form">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table><br>
    <center>
      <input type="submit" value="send" id="send" 
          onclick="return Pload('new_thread_form', '{% url post_thread %}');"/>
    </center>
    <script type="text/javascript">
    $("#id_document").val({{ params.doc }});
    $("#id_page").val({{ params.page }});
    </script>
</form>

<p>This thread is about the page : </p>
<img style="margin-left: 30px; margin-right: 30px; background-color: white"
     src="{% url download_page params.doc params.page %}">
