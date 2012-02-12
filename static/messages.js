function new_thread_box(course, doc, page) {
	overlay_reset();
	overlay_title("New Thread");
	overlay_show();
	$('#overlay_content').load('/msg/new_thread/' + course + '/' + doc + '/' + page, overlay_refresh);
}

function list_thread(course, doc, page) {
	overlay_reset();
	overlay_title("Thread about the page " + page);
	overlay_show();
	$('#overlay_content').load('/msg/list_thread/' + course + '/' + doc + '/' + page, overlay_refresh);
}

function preview_thread(id, place) {
	if ($('#prev' + id).length > 0)
		return;
	$('#' + place).after('<tr id="tr_thread_' + id + '"><td class="min2"></td><td colspan=2><div id="prev'+id+'">loading..</div></td></tr>');
	$('#prev' + id).load('/msg/prev_thread/' + id, overlay_refresh); // FIXME why overlay_refresh?
}
