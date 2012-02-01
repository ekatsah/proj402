<form enctype="multipart/form-data" method="post" action="" id="upload_form">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table><br>
    <center><input type="submit" value="upload" id="upload"/></center>
</form>
