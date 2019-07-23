from django import forms
from .models import Mentee, Mentor, Blog

class MenteeForm(forms.ModelForm):
    
    class Meta:
        model = Mentee
        fields = ('nama', 'quotes', 'profile_pic')

class MentorForm(forms.ModelForm):

    class Meta:
        model = Mentor
        fields = ('nama', 'experience', 'quotes', 'profile_pic')

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('judul', 'gambar', 'tanggal', 'comment', 'desc')