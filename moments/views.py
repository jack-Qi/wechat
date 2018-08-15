from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from django.http import HttpResponse
from . import models

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

def home(request):
	return render_to_response("homepage.html")

@login_required
def show_user(request):
	tim = {"name":"Jack Json",
			"region":"shanghai",
			"pic":"cat.jpeg",
			"motto":"I love Python",
			"album":"qijia.jpg"
	}
	return render_to_response("user.html",{"user":tim})

@login_required
def show_status(request):
	statuses = models.Status.objects.all()
	return render_to_response("status.html",{"statuses":statuses})

@login_required
def submit_timeline(request):
	origin_user = request.user
	user = models.WeChatUser.objects.get(user=origin_user)
	text = request.POST.get('text')
	
	upload_file = request.FILES.get('pic','')

	if upload_file:
		file_name = upload_file.name
		with open('./moments/static/image/{}'.format(file_name), 'wb') as fh:
			for block in upload_file.chunks():
				fh.write(block)
	else:
		file_name = ''

	if text:
		status = models.Status(text=text,user=user,pics=file_name)
		status.save()
		return redirect('/status')

	#return render_to_response("my_post.html", context_instance=RequestContext(request))
	return render(request,"my_post.html")
