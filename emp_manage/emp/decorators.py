from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('show')
   			# return view_func(request, *args, **kwargs)
		else:
			# return redirect('login/')
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'employee':
			return redirect('show')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function

def role_required(allowed_roles=[]):
    def decorator(view_func): 
        def wrap(request, *args, **kwargs):
            if request.role is allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator