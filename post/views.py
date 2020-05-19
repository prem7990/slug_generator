from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def home(request):
	obj= Post.objects.all()
	return render(request,'index.html',{'obj':obj})

def details(request,slug_id):
	post = Post.objects.filter(slug=slug_id)
	if post.exists():
		post=post.first()
	else:
		return HttpResponse("<h1>Page not found</h1>")
	return render(request,'details.html',{'post':post})