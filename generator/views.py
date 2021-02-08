from django.shortcuts import render

from random import randint , choice


def home(request):
    return render(request,'generator/home.html')



def password(request):
    len = int(request.GET.get('length',8))
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyz'
    characters2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    characters3 = '123456789'
    characters4 = '()&!=-@#./\*~'
    if ( request.GET.get('Upercase') and request.GET.get('numbers') and request.GET.get('special_sign') ):
        for i in range(len):
            password += choice(characters+characters2+characters3+characters4)
    elif ( request.GET.get('Upercase') and request.GET.get('numbers')):
        for i in range(len):
            password += choice(characters+characters2+characters3)
    elif ( request.GET.get('Upercase') and request.GET.get('special_sign')):
        for i in range(len):
            password += choice(characters+characters2+characters4)
    elif ( request.GET.get('numbers') and request.GET.get('special_sign')):
        for i in range(len):
            password += choice(characters3+characters4)
    elif request.GET.get('Upercase'):
        for i in range(len):
            password += choice(characters+characters2)
    elif (request.GET.get('special_sign') ):
        for i in range(len):
            password += choice(characters+characters4)
    elif (request.GET.get('numbers')):
        for i in range(len):
            password += choice(characters+characters3)
    else:
        for  i in range(len):
            password += choice(characters)

    return render(request,'generator/password.html',{ 'password' : password })




def about_me(request):
    return render(request,'generator/aboutme.html')
