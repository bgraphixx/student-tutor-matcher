from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.forms import ModelForm
#import django admin user model
from django.contrib.auth.models import User
from .models import Students

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':('Enter your First Name')})
        self.fields['last_name'].widget.attrs.update({'placeholder':('Enter your Last Name')})
        self.fields['email'].widget.attrs.update({'placeholder':('Enter your Email Address')})
        self.fields['username'].widget.attrs.update({'placeholder':('Enter your username ')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Enter your Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Confirm your password')})
        self.fields['password1'].widget.attrs.update({'class':('form-control my-3 p-2')}) 
        self.fields['password2'].widget.attrs.update({'class':('form-control my-3 p-2')})  

        password1 = forms.CharField(
            label= " ",
            widget= forms.PasswordInput(attrs={'class': 'form-control my-3 p-2' , 'title': 'Please Password must be 8 characters long consisting of at least a small letter, capital letter and number', 'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}),
        )
        password2 = forms.CharField(
            label= " ",
            widget= forms.PasswordInput(attrs={'class': 'form-control my-3 p-2' , 'title': 'Please Password must be 8 characters long consisting of at least a small letter, capital letter and number', 'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}),
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control my-3 p-2', 'title': 'Please fill field',}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control my-3 p-2', 'title': 'Please fill field'}), 
            'email' : forms.EmailInput(attrs={'class': 'form-control my-3 p-2', 'title': 'Invalid email', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}), 
            'username' : forms.TextInput(attrs={'class': 'form-control my-3 p-2' , 'title': 'Please fill field'}),
        }

class InputForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}), 
            'student_id' : forms.NumberInput(attrs={'class': 'form-control'}), 
            'gender' : forms.Select(attrs={'class': 'form-control'}),
            'age' : forms.Select(attrs={'class': 'form-control'}),
            'parental_status' : forms.Select(attrs={'class': 'form-control'}),
            'guardian' : forms.Select(attrs={'class': 'form-control'}),
            'intention' : forms.Select(attrs={'class': 'form-control'}),
            'romantic' : forms.Select(attrs={'class': 'form-control'}),
            'extra_curr' : forms.Select(attrs={'class': 'form-control'}),
            'alcohol_cons' : forms.Select(attrs={'class': 'form-control'}),
            'no_of_failures' : forms.Select(attrs={'class': 'form-control'}),
            'grade1' : forms.NumberInput(attrs={'class': 'form-control'}), 
            'grade2' : forms.NumberInput(attrs={'class': 'form-control'}), 
            'grade3' : forms.NumberInput(attrs={'class': 'form-control'}),
        }

# class CompactForm(ModelForm):
#     class Meta:
#         fields = '__all__'
#         labels ={
#             'student' : 'Select Student',
#             'learning_styles' : 'Select Learning Style',
#             'personality_styles' : 'Select Personality Style',
#             'area_of_interests' : 'Select Area of Interest',
#         }
#         widgets = {
#             'student' : forms.Select(attrs={'class': 'form-control'}),
#             'learning_styles' : forms.Select(attrs={'class': 'form-control'}),
#             'personality_styles' : forms.Select(attrs={'class': 'form-control'}),
#             'area_of_interests' : forms.Select(attrs={'class': 'form-control'}),
#         }
#         model = Pass
        
# class InputForm(forms.Form):
#     GENDER = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     AGE = (
#         ('15', '15'),
#         ('16', '16'),
#         ('17', '17'),
#         ('18', '18'),
#         ('19', '19'),
#         ('20', '20'),
#         ('21', '21'),
#         ('22', '22'),
#     )
#     PARENTAL_STATUS = (
#         ('Togther', 'Together'),
#         ('Apart', 'Apart'),
#     )
#     GUARDIAN = (
#         ('Father', 'Father'),
#         ('Mother', 'Mother'),
#         ('Other', 'Other'),
#     )
#     INTENTION = (
#         ('Yes', 'Yes'),
#         ('No', 'No'),
#     )
#     ROMANTIC = (
#        ('Yes', 'Yes'),
#         ('No', 'No'),
#     )
#     EXTRA = (
#         ('Yes', 'Yes'),
#         ('No', 'No'),
#     )
#     ALCOHOL = (
#         ('0', '0'),
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#     )
#     FAILURES = (
#         ('0', '0'),
#         ('1', '1'),
#         ('2', '2'),
#     )
      
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}), label= "First Name", max_length = 200)
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}), label= "Last Name", max_length = 200)
#     student_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label= "Student ID")
#     gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), label= "Gender", choices=GENDER)
#     age = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), label= "Age", choices=AGE)
#     parental_status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Parental Status", choices=PARENTAL_STATUS)
#     guardian = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Guardian",choices=GUARDIAN)
#     intention = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Intention to pursue higher education",choices=INTENTION)
#     romantic = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Romantic Relationships", choices=ROMANTIC)
#     extra_curr = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Extra curricular activites",choices=EXTRA)
#     alcohol_cons = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Alcohol Consumptions during weekdays",choices=ALCOHOL)
#     no_of_failures = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label= "Number of Failures", choices=FAILURES)
#     grade1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label= "Grade 1",)
#     grade2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label= "Grade 2",)
#     grade3 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label= "Grade 3",)

#     class Meta:
#         model = Students