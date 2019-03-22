from django.shortcuts import render
from .forms import PostForm ,qwe,addcomment,sea
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import post ,Like , Comment
from django.db.models import Q
from django.http import JsonResponse
from django.db.models import Count
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import auth_login
alert = False

def ava(request):
    return render(request, 'registration/profile.html')
def agreement(request):
    return render(request, 'registration/agreement.html')

def settings(request):
    form = sea()
    if request.user.is_authenticated:
        return render(request,'registration/setting.html',{'form': form})
    else:
        form = sea()
        form2 = AuthenticationForm()
        return  render(request, 'registration/login.html', {'form': form , 'form2': form2 })


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/list/')
    else:
        form2 = AuthenticationForm()
        form = sea()
        return render(request, 'registration/login.html', {'form': form , 'form2': form2 })


def user_new(request):
    if request.method == "POST":
        form1 = PostForm(request.POST)
        form = sea()
        if form1.is_valid():
            print(form1.cleaned_data)
            user = User.objects.create_user(form1.cleaned_data['username'],form1.cleaned_data['email'], form1.cleaned_data['password'])

            user.first_name = form1.cleaned_data['first_name']
            user.last_name =  form1.cleaned_data['last_name']
            user.save()
            form2 = AuthenticationForm()
            return redirect('http://dearproblems.herokuapp.com/login/' , {'form2':form2})
        else:
            return render(request, 'registration/post_edit.html', {'form1': form1, 'form': form})
    else:
        form = sea()
        form1 = PostForm()
        return render(request, 'registration/post_edit.html', {'form1': form1,'form': form })



def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def logout_view(request):
    logout(request)
    return redirect("http://dearproblems.herokuapp.com/")


def profile(request):
    if request.user.is_authenticated:
        form = sea()
        a = User.objects.get(username=request.user.username)
        p = post.objects.filter(user__username=a.username)
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form,"u": a }
        return render(request, 'registration/new.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/', {'form2': form2})

def profile1(request):
    if request.user.is_authenticated:
        form = sea()
        a = User.objects.get(username=request.user.username)
        p = post.objects.filter(comment__user=a.pk)
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form,"u": a }
        return render(request, 'registration/new.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2})

def profile2(request):
    if request.user.is_authenticated:
        form = sea()
        a = User.objects.get(username=request.user.username)
        p = post.objects.filter(like__user=a.pk)
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form,"u": a }
        return render(request, 'registration/new.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2})





def formpost(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = qwe(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.user = User.objects.get(username=request.user.username)
                p.title = form.cleaned_data['title']
                p.description = form.cleaned_data['description']
                p.save()
                global alert
                alert = True
                return redirect('http://dearproblems.herokuapp.com/list/')
        else :
            form = sea()
            form1 = qwe()
            return render(request,'registration/post_form.html',{'form':form ,'form1': form1 })
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2})

def postlist(request):
    if request.user.is_authenticated:
        form=sea()
        #p = post.objects.all()
        p = post.objects.annotate(like_count=Count('like')).annotate(comment_count=Count('comment')).order_by('-like_count','-comment_count')
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I=zip(w,n,c,u)
        global alert
        if(alert == True):
            data_for_alert = "Your post has been published."
        else:
            data_for_alert = False
        alert = False
        context = {"z":I,"form":form ,"data_for_alert": data_for_alert }
        return render(request, 'registration/my_book_list.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2})




def post_detail_view(request,id):
    if request.user.is_authenticated:
        form = sea()
        try:
            p = post.objects.get(id=id)
        except post.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
        c = p.comment_set.all()
        context_switch = []
        inc = 1
        for i in c:
            if inc == 1:
                inc = 0
            else:
                inc = 1
            context_switch.append(inc)

        comment =[]
        user_of_comment =[]
        for i in c:
            comment1 = Comment.objects.get(id=i.id)
            user_of_comment1 = User.objects.get(comment__id = i.id)
            comment.append(comment1)
            user_of_comment.append(user_of_comment1)
        if (comment):
            no_1 = False
        else:
            no_1 = True
        print(context_switch)
        user_and_comment = zip(comment,user_of_comment, context_switch)
        form_comment = addcomment()
        context = {"post": p ,"u_and_c" : user_and_comment , "form_comment": form_comment ,"form": form ,"no_c": no_1}
        return render(request,'registration/add_comment.html',context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })

def add_like(request):
    if request.user.is_authenticated:
        id = request.GET.get('id', None)

        new_like, created = Like.objects.get_or_create(user=request.user, like_id=id)

        if not created:
            data=  { "w":"already liked"}
        else:
            p = post.objects.get(id=id)
            n = p.like_set.all().count()
            data = {"w":n}

        return JsonResponse(data)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })

def add_comment(request, id):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = addcomment(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.user = User.objects.get(username=request.user.username)
                p.comment = form.cleaned_data['comment']
                p.post = post.objects.get(id=id)
                p.save()
                return redirect('http://dearproblems.herokuapp.com/'+ str(id) +"/")
        else :
            return redirect('http://dearproblems.herokuapp.com/addcomment/' + str(id) +"/")
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })

def profile_others(request,id):
    if request.user.is_authenticated:
        form = sea()
        try:
            a = User.objects.get(id=id)
            p = post.objects.filter(user__id=id)
        except User.DoesNotExist or post.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form, "u": a}
        return render(request, 'registration/new1.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })

def profile_others1(request,id):
    if request.user.is_authenticated:
        form = sea()

        try:
            a = User.objects.get(id=id)
            p = post.objects.filter(comment__user__id=id)
        except User.DoesNotExist or post.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form, "u": a}
        return render(request, 'registration/new1.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })

def profile_others2(request,id):
    if request.user.is_authenticated:
        form = sea()
        try:
            p = post.objects.filter(like__user__id=id)
            a = User.objects.get(id=id)
        except User.DoesNotExist or post.DoesNotExist:
            raise Http404("no you r on wrong track")

        w = []
        n = []
        c = []
        u = []
        for i in p:
            w1 = post.objects.get(id=i.id)
            n1 = w1.like_set.all().count()
            c1 = w1.comment_set.all().count()
            u1 = User.objects.get(post__id=i.id)
            w.append(w1)
            n.append(n1)
            c.append(c1)
            u.append(u1)
        I = zip(w, n, c, u)
        context = {"z": I, "form": form, "u": a}
        return render(request, 'registration/new1.html', context)
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })








def searchlist(request ):
    if request.user.is_authenticated:
        form = sea(request.GET)
        if form.is_valid():
            w = []
            n = []
            c = []
            u = []
            name = form.cleaned_data['q']
            p = post.objects.filter(Q(title__icontains=name) |
            Q(description__icontains=name) |
            Q(user__username__icontains=name)|
            Q(user__first_name__icontains=name) |
            Q(user__last_name__icontains=name)).annotate(like_count=Count('like')).annotate(comment_count=Count('comment')).order_by('-like_count','-comment_count')
            for i in p:
                w1 = post.objects.get(id=i.id)
                n1 = w1.like_set.all().count()
                c1 = w1.comment_set.all().count()
                u1 = User.objects.get(post__id=i.id)
                w.append(w1)
                n.append(n1)
                c.append(c1)
                u.append(u1)
            I = zip(w, n, c, u)
            context = {"z": I,"icon": True }
            return render(request, 'registration/my_book_list.html', context)
        else:
            return redirect("http://dearproblems.herokuapp.com/list/")
    else:
        form2 = AuthenticationForm()
        return redirect('http://dearproblems.herokuapp.com/login/',{'form2': form2 })













