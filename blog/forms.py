from django import forms
from .models import Comment

# نام کلاس باید CommentForm باشد (حرف اول بزرگ)
class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body') # این خط هم که قبلا ارور داشت یادتان نرود
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل (اختیاری)'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'نظر خود را بنویسید...'}),
        }