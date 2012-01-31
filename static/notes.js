function new_thread_box(doc, page) {
	overlay_reset();
	overlay_title("New Thread");
	overlay_show();
	$('#overlay_content').load('/note/new_thread/' + doc + '/' + page, overlay_refresh);
}