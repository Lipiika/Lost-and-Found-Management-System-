from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


# -------------------------------
# LOGIN VIEW
# -------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'system/login.html')


# -------------------------------
# SIGNUP VIEW
# -------------------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('user_dashboard')

    return render(request, 'system/signup.html')


# -------------------------------
# USER DASHBOARD
# -------------------------------
@login_required
@user_passes_test(lambda u: not u.is_staff)
def user_dashboard(request):
    return render(request, 'system/user_dashboard.html')


# -------------------------------
# ADMIN DASHBOARD
# -------------------------------
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'system/admin_dashboard.html')


# -------------------------------
# LOGOUT VIEW
# -------------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

from .forms import LostItemForm
from .models import LostItem

@login_required
@user_passes_test(lambda u: not u.is_staff)
def user_dashboard(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.save()
            return redirect('user_dashboard')
    else:
        form = LostItemForm()

    items = LostItem.objects.all().order_by('-date_lost')[:10]  # show latest 10
    return render(request, 'system/user_dashboard.html', {'form': form, 'items': items})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    from .models import LostItem
    from django.contrib.auth.models import User

    users = User.objects.filter(is_staff=False).count()
    lost_items = LostItem.objects.count()
    latest_items = LostItem.objects.order_by('-date_lost')[:5]

    context = {
        'users': users,
        'lost_items': lost_items,
        'latest_items': latest_items,
    }
    return render(request, 'system/admin_dashboard.html', context)


from django.contrib.auth.models import User
from .models import LostItem

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    user_count = User.objects.filter(is_staff=False).count()
    item_count = LostItem.objects.count()
    recent_items = LostItem.objects.all().order_by('-date_lost')[:5]

    return render(request, 'system/admin_dashboard.html', {
        'user_count': user_count,
        'item_count': item_count,
        'recent_items': recent_items
    })
