<form id="new_thread_form">
<table>
<tr><td>Subject:</td><td><input id="thread_title" style="width: 400px"/></td></tr>
<tr><td valign="top">Message:</td>
    <td><textarea id="thread_body" style="width: 400px; height: 200px;"></textarea></td></tr>
<tr><td></td><td align="right"><input type="submit" value="send"/></td></tr>
</table>

<p>This thread is about the page : </p>
<img style="margin-left: 30px; margin-right: 30px"
     src="{% url download_page params.doc params.page %}">
</form>
