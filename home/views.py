from django.shortcuts import render,redirect
from home.forms import ModelcustomForms
from home.forms import customForms
from home.forms import library
from home.forms import Searchform
from django.contrib import messages


# Create your views here.
def home_view(request):
    return render(request,'home.html')
def home1(request):
    return render(request,'design.html')
def home2(request):
    return render(request,'login.html')
def home3(request):
    return render(request,'signup.html')

def form_view(request):
    msg=''
    if request.method=='POST':
        form=customForms(request.POST)
        if form.is_valid():
            lib=library.objects.create(
                Studentname=form.cleaned_data.get('Studentname'),
                Branch=form.cleaned_data.get('Branch'),
                IssueDate=form.cleaned_data.get('IssueDate'),
                SubmissionDate=form.cleaned_data.get('SubmissionDate'),
                IssuedBooks=form.cleaned_data.get('IssuedBooks')
            )
            lib.save()
            msg='Data Successfully Added'
           
        else:
            msg=form.errors
    else:
        form=customForms()
    return render(request,'forms.html',{"msg":msg,"forms":form,})



def search(request):
    lib=''
    if request.method=='POST':
        form=Searchform(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            lib=library.objects.filter(Studentname_contains=q)
            return render(request,'data.html',{'library':lib})
    else:
        form=Searchform()
        lib=library.objects.all()
    return render(request,'data.html',{'library':lib,'form':form})



def deleterecord(request,Studentname):
    lib=library.objects.get(Studentname=Studentname)
    lib.delete()
    messages.success(request,'DELETED '+Studentname+ ' SUCCESSFULLY')
    return redirect('/search')

def editrecord(request,Studentname):
    lib=library.objects.get(Studentname=Studentname)
    if request.method=="POST":
        form=ModelcustomForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully!!')
            return redirect('/search')
    else:
        form=ModelcustomForms(instance=lib)
    return render(request,'edit.html',{'library':lib,'form':form})


    
        


            #  lib=library(
            #     Studentname=form.cleaned_data.get('Studentname'),
            #     Branch=form.cleaned_data.get('Branch'),
            #     IssueDate=form.cleaned_data.get('IssueDate'),
            #     SubmissionDate=form.cleaned_data.get('SubmissionDate'),
            #     IssuedBooks=form.cleaned_data.get('IssuedBooks')
            # ) 
 