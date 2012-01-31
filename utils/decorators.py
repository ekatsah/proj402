from django.http import HttpResponseRedirect

# Ajax rewrite.
def AR(function):
	def check_ajax(request, *args, **kwargs):
		if (request.is_ajax()):
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/zoidberg#' + request.path)
	return check_ajax