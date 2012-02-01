from django.http import HttpResponse, HttpResponseRedirect

# Ajax rewrite.
def AR(function):
	def check_ajax(request, *args, **kwargs):
		if (request.is_ajax()):
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/zoidberg#' + request.path)
	return check_ajax

# enforce a post request
def enforce_post(function):
	def check_post(request, *args, **kwargs):
		if request.method == 'POST':
			return function(request, *args, **kwargs)
		else:
			return HttpResponse("Error: Not a post request")
	return check_post