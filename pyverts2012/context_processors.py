def theme(request):
    try:
    	return dict(theme=request.session["theme"])
    except KeyError:
    	return dict(theme="content.html")