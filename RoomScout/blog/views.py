from django.shortcuts import render


def blogs(request):
	return render(request, 'blog/blog.html')
