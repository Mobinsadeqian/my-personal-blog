from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm # ⚠️ مطمئن شوید که CommentForm با حروف بزرگ باشد

# تابع برای نمایش لیست پست‌ها
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# تابع برای نمایش جزئیات پست و مدیریت فرم کامنت
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 1. گرفتن کامنت‌های فعال برای نمایش
    comments = post.comments.all().filter(active=True) # ✅ جایگزین احتمالی
    
    new_comment = None
    
    if request.method == 'POST':
        # اگر کاربر فرم را ارسال کرده است
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # یک آبجکت کامنت می‌سازیم اما هنوز در دیتابیس ذخیره نمی‌کنیم
            new_comment = comment_form.save(commit=False)
            
            # کامنت را به پست مربوطه وصل می‌کنیم
            new_comment.post = post
            
            # کامنت را ذخیره می‌کنیم (active=False پیش‌فرض)
            new_comment.save()
            
            # ریدایرکت برای جلوگیری از ارسال مجدد فرم در صورت رفرش صفحه
            return redirect('post_detail', pk=post.pk) 
            
    else:
        # اگر متد GET است (فقط نمایش صفحه)
        comment_form = CommentForm()

    return render(request, 
                  'blog/post_detail.html', 
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})