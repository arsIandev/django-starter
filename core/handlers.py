from django.shortcuts import render


def handler400(request, exception=None):
    template_name = "handler/400.html"
    context = {
        'title': "Error 400 – Bad Request",
        'status_code': 400,
        'message': "You've sent a bad request."
    }
    return render(request, template_name, context)


def handler403(request, exception=None):
    template_name = "handler/403.html"
    context = {
        'title': "Error 403 – Forbidden",
        'status_code': 403,
        'message': "You don’t have permission to access this url on this server."
    }
    return render(request, template_name, context)



def handler404(request, exception=None):
    template_name = "handler/404.html"
    context = {
       'title': "Error 404 – Page Not Found",
       'status_code': 404,
       'message': "The page you requested was not found."
    }
    return render(request, template_name, context)


def handler500(request, exception=None):
    template_name = "handler/500.html"
    context = {
        'title': "Error 500 – Server Error",
        'status_code': 500,
        'message': "Oops, something went wrong."
    }
    return render(request, template_name, context)
