from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# def home(request):
#     return render(request,'stack/base.html')

def signup(request):
    if request.method=='POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()       
    else:
        form = UserForm()
    return render(request,'stack/signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            
    else:
        form=AuthenticationForm()
    return render(request,'stack/signin.html',{'form':form})

def question(request):
    if request.method == 'POST':
        que=QuestionForm(request.POST)
        if que.is_valid():
            data = que.save(commit=False)
            data.created_by = request.user
            data.save()
            return redirect('/')
    else:
        que=QuestionForm()
    return render(request,'stack/question.html',{'question':que})



def reply(request):
    if request.method == "POST":
        rep=ReplyForm(request.POST)

        rep.save()
    else:
        rep=ReplyForm()
    return render(request,'stack/reply.html',{'rep':rep})

# @login_required(login_url="stack:signin")
def dashboard(request):
    # import pdb; pdb.set_trace()
    que=Questions.objects.order_by("-created_at")
    searchitem = request.GET.get('searchitem',None)
    id_value = request.POST.get("question", None)
    if searchitem:
        que=Questions.objects.filter(name__icontains=searchitem)
    
    if "Like" in request.POST:
            question_value = Questions.objects.get(id=id_value)
            question_value.up_vote += 1
            question_value.save()
        
    if "dislike" in request.POST:
        question_value = Questions.objects.get(id=id_value)
        question_value.down_vote += 1
        question_value.save()    
    return render(request, "stack/index.html",{'que':que})


def answer(request,pk):
    get_question = Questions.objects.get(id=pk)
    id_value = request.POST.get("answer", None)
    if request.method == "POST":
        ans=AnswerForm(request.POST)
        if ans.is_valid():
            data=ans.save(commit=False)
            data.created_by = request.user
            data.questions=get_question
            data.save()
            return redirect('/')
    else:
        ans=AnswerForm()
    if "Like" in request.POST:
            question_value = Answer.objects.get(id=id_value)
            question_value.up_vote += 1
            question_value.save()
        
    if "dislike" in request.POST:
        question_value = Answer.objects.get(id=id_value)
        question_value.downvote += 1
        question_value.save()        
    return render(request,'stack/answer.html',{'form':ans,'questions':get_question})


def get_reply(request,pk):
    answers=Answer.objects.get(id=pk)
    if request.method=="POST":
        form=ReplyForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.created_by=request.user
            data.answer= answers
            form.save()
            return redirect('/')
    else:
        form=AnswerForm()
      
    return render(request,"pages/reply.html",{
        "form":form,
        'answers':answers
    })

def profile(request,pk):
    user= User.objects.get(id=pk)
    print(user)
    return render(request,'stack/profile.html',{'user':user})

def delete_question(request,pk):
    que=Questions.objects.get(id=pk)   
    que.delete()       
    return redirect('/')
    
def update_question(request,pk):
    if request.method == "POST":
        que=Questions.objects.get(id=pk)
        form=QuestionForm(request.POST,instance=que)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    else:
        que=Questions.objects.get(id=pk)
        form=QuestionForm(instance=que)
    return render(request,'stack/updatequestion.html',{'question':que,'form':form}) 

def logout_user(request):
    logout(request)
    return redirect("/")

def reply_to(request,pk):
    answers=Answer.objects.get(id=pk)
    if request.method=="POST":
        form=ReplyForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.created_by=request.user
            data.answer= answers
            form.save()
            return redirect('/')
    else:
        form=AnswerForm()
      
    return render(request,"stack/replay_to.html",{
        "form":form,
        'answers':answers
    })


