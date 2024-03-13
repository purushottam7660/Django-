# from django.shortcuts import render
# from studentapp.forms import StudentForm

# def index(request):
#     form=StudentForm()
#     if request.method=='POST':
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             print("Success")

#     return render(request,"index.html", {'form':form})
from django.shortcuts import render
from studentapp.forms import Student

dr