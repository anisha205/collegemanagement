from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        
    labels = {
        'student_id' : 'student id',
        'student_name' : 'Student name',
        'student_phone' : 'Student phone',
        'student_email' : 'Student email',
        'student_address' : 'Student  address',
        'student_place' : 'Student place'


        
    }