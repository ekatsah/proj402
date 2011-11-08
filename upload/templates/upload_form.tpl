<form enctype="multipart/form-data" method="post" action="/upload/put">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="upload" id="upload"/>
</form>
