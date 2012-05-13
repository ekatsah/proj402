from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from courses.models import Course
from users.models import CourseFollow, CreateUserForm

def mask_welcome(request):
    up = request.user.profile
    up.welcome = False
    up.save()
    return HttpResponse('ok', 'text/html')

def get_courses(request):
    return render(request, 'user_courses.tpl', {'guess': list()})

def follow(request):
    courses = request.POST.get('courses', '')
    if len(courses) == 0:
        return HttpResponse('invalid request is invalid', 'text/html')
    courses = courses.split('+')
    
    for course in courses:
        try:
            course = Course.objects.get(slug=course)
        except:
            continue
        
        up = request.user.profile
        # already following
        if len(up.courses.filter(course=course)):
            continue
        cf = CourseFollow.objects.create(course=course)
        up.courses.add(cf)
    
    return HttpResponse('ok', 'text/html')

def modo(uid, flag):
    u = get_object_or_404(User, pk=uid)
    up = u.get_profile()
    up.moderate = flag
    up.save()
    return HttpResponse('ok', 'text/html')

def set_modo(request, uid):
    return modo(uid, True)

def unset_modo(request, uid):
    return modo(uid, False)

def new_user(request):
    print "plop"
    form = CreateUserForm(request.POST)
    print "plop2"
    if form.is_valid():
        print "valid"
        data = form.cleaned_data
        print "clean"
        try:
            user = User.objects.create_user(data['username'], data['email'],
                                            data['password'])
        except Exception as e:
            return HttpResponse("Error: username not unique")
        print "user"
        user.last_name = data['last_name']
        user.first_name = data['first_name']
        user.save()
        print "saved user"
        user_profile = user.profile
        user_profile.registration = data['registration']
        user_profile.section = data['fac_id'] + ':' + data['section']
        user_profile.comment = data['comment']
        user_profile.save()
        user.save()
        print "end of it"
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")
