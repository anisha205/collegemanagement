from django.shortcuts import render,redirect
from django.views import View
from account.models import Staff,Contact
from home.models import Students
from.forms import StudentForm
from django.contrib import messages

# from home.models import StudentForm


# Create your views here.
class Profile(View):
    def get(self,request):
        return render(request,'profile.html')
class Conformation(View):
    def get(self,request):
        std=Students.objects.all()
        return render(request,'conformation.html',{'form':std})    

class Loginhome(View):
    def get(self,request):
        return render(request,'loginhome.html')
class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'editprofile.html',{'form':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method == 'POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"email id already exists")
                        return render(request,'editprofile.html',{'form':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(name=request.session['name'])
                return render(request,'profile.html',{'customer':customer})
                





class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'eniqury.html',{'form':customer})
class Staffs(View):
    def get(self,request):
        staff=Staff.objects.all()
        return render(request,'staff.html',{'form':staff})
    

class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})    

            
class students(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'students.html',{'form':std1})
    def post(self,request):
        if request.method == "POST":
            std1 = StudentForm(request.POST)
            if std1.is_valid():
               std1.save()
               std2=Students.objects.all()
               return render(request,'conformation.html',{'form':std2})
            else:
                print("form not valid")
                return redirect("conformation") 
class Delete(View):
    def get(self,request):
        delete=request.GET['delete'] 
        Students.objects.filter(student_id=delete) .delete()
        std2=Students.objects.all()
        return render(request,'Conformation.html',{'form':std2})       







class Edit(View):
    def get(self,request):
        edit1=request.GET['edit'] 
        edit=Students.objects.filter(student_id=edit1) 
        return render(request,'edit.html',{'forms':edit}) 
    def post(self,request):
        edit1=request.GET['edit'] 
        if request.method == 'POST':
            if Students.objects.filter(student_id=edit1).exists():
                if request.POST['student_address']:
                    print(request.POST['student_address'])
                    Students.objects.filter(student_id=edit1).update(student_address=request.POST['student_address'])
                if request.POST['student_place']:
                    Students.objects.filter(student_id=edit1).update(student_place=request.POST['student_place'])
                if request.POST['student_name']: 
                    Students.objects.filter(student_id=edit1).update(student_name=request.POST['student_name'])
                if request.POST['student_email']: 
                    Students.objects.filter(student_id=edit1).update(student_email=request.POST['student_email'])
                if request.POST['student_phone']:    
                    Students.objects.filter(student_id=edit1).update(student_phone=request.POST['student_phone'])
                std2=Students.objects.all()
                return render(request,'conformation.html',{'form':std2})


    

   

