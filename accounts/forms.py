from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserRegistration, UserRUCF1, UserRUM,UserRUCF2,UserRUCA1

class UserRUCF1Form(forms.ModelForm):
    f1form = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone', 'id': 'f1form', 'required': 'true'}))
    class Meta:
        model = UserRUCF1
        fields = ['f1form']
class UserRUMForm(forms.ModelForm):
    rumform = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone', 'id': 'rumform', 'required': 'true'}))
    class Meta:
        model = UserRUM
        fields = ['rumform']
class UserRUCF2Form(forms.ModelForm):

    f2form = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone', 'id': 'f2form', 'required': 'true'}))

    class Meta:
        model = UserRUCF2
        fields = ['f2form']

class UserRUCA1Form(forms.ModelForm):

    a1form = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone', 'id': 'a1form', 'required': 'true'}))

    class Meta:
        model = UserRUCA1
        fields = ['a1form']

class CreateStudentForm(forms.Form):
    adm_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'adm_number', 'required': 'true', 'placeholder': 'Admision Number'}))


class UserRegistrationForm(forms.ModelForm):
    """Form definition for UserRegistration."""

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'email', 'required': 'true'}))
    joined_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'date', 'required': 'true'}))
    gender = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'gender', 'tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    salutation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'salutation', 'tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    religion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'religion', 'tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    mstatus = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'mstatus', 'tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'accademic_year', 'pattern': '-?[0-9]*(\.[0-9]+)?', 'required': 'true'}))
    dob = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'dateOfBirth', 'required': 'true'}))
    profile_picture = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone', 'id': 'picture', 'accept': 'image/*', 'required': 'true'}))

    class Meta:
        
        """Meta definition for UserRegistrationform."""

        model = UserRegistration
        fields = ['email','joined_date','gender','salutation','religion','mstatus','phone_number','dob','profile_picture']


class RegistrationForm(forms.ModelForm):
    index_number_year  = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'index_number_year', 'required': 'true', 'placeholder': 'Index Number/Year'}))

    student_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'student_name', 'required': 'true', 'placeholder': 'Student Name'}))

    box = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'box', 'placeholder': 'P.O BOX Number'}))

    school = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'school', 'required': 'true', 'placeholder': 'School'}))

    town = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'town', 'placeholder': 'Town'}))

    postalcode = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'postalcode', 'placeholder': 'Postal Code (with name if available)'}))


    class Meta:
        
        """Meta definition for UserRegistrationform."""

        model = UserRegistration
        fields = ['index_number_year', 'student_name', 'box', 'school', 'town', 'postalcode']
# class StudentProfileForm(forms.ModelForm):
#     """Form definition for StudentProfile."""
#     first_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
#     surname = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'mdl-textfield__input', 'id': 'surname', 'required': 'true'}))
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
#     adm_number = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'mdl-textfield__input', 'id': 'adm_number', 'required': 'true'}))

#     class Meta:
#         """Meta definition for StudentProfileform."""

#         model = StudentProfile
#         fields = ['first_name','surname','last_name','adm_number']

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.TextInput(
#         attrs={'class': 'input100', 'id': 'id_email', 'placeholder': 'Email programme', 'required': 'true'}))
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'input100', 'id': 'id_password1','placeholder':'Password', 'required': 'true'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'input100', 'id': 'id_password2','placeholder':'Confirm Password', 'required': 'true'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password', 'placeholder':'Password','required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)
