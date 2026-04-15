# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Task, Profile
#
#
# # ---------------- AUTH ---------------- #
#
# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm = request.POST.get("confirm_password")
#
#         if password != confirm:
#             messages.error(request, "Passwords do not match")
#
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#
#         else:
#             User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password
#             )
#             messages.success(request, "Account created successfully!")
#             return redirect('login')
#
#     return render(request, 'Tsignup.html')
#
#
# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Invalid username or password")
#
#     return render(request, 'Tlogin.html')
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('login')
#
#
# # ---------------- DASHBOARD ---------------- #
#
# @login_required
# def dashboard(request):
#     tasks = Task.objects.filter(user=request.user)
#
#     total = tasks.count()
#     completed = tasks.filter(completed=True).count()
#     pending = tasks.filter(completed=False).count()
#
#     return render(request, 'Tindex.html', {
#         'tasks': tasks,
#         'total': total,
#         'completed': completed,
#         'pending': pending,
#         'chart_completed': completed,
#         'chart_pending': pending
#     })
#
#
# # ---------------- ADD TASK ---------------- #
#
# @login_required
# def add_task(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         category = request.POST.get("category")
#         deadline = request.POST.get("deadline")
#         priority = request.POST.get("priority")
#
#         if not title or not description:
#             messages.error(request, "All fields are required")
#             return redirect('add_task')
#
#         Task.objects.create(
#             user=request.user,
#             title=title,
#             description=description,
#             category=category,
#             deadline=deadline if deadline else None,
#             priority=priority
#         )
#
#         messages.success(request, "Task added successfully!")
#         return redirect('dashboard')
#
#     return render(request, 'Taddtask.html')
#
#
# # ---------------- COMPLETE TASK ---------------- #
#
# @login_required
# def mark_completed(request, task_id):
#     task = get_object_or_404(Task, id=task_id, user=request.user)
#     task.completed = True
#     task.save()
#     return redirect('dashboard')
#
#
# # ---------------- PROFILE ---------------- #
#
# @login_required
# def profile(request):
#     return render(request, 'Tprofile.html', {
#         'user': request.user,
#         'profile': request.user.profile
#     })
#
#
# @login_required
# def edit_profile(request):
#     user = request.user
#     profile = user.profile
#
#     if request.method == "POST":
#         new_username = request.POST.get("username")
#
#         # Username validation
#         if User.objects.exclude(id=user.id).filter(username=new_username).exists():
#             messages.error(request, "Username already taken")
#             return redirect('edit_profile')
#
#         user.first_name = request.POST.get("name")
#         user.email = request.POST.get("email")
#         user.username = new_username
#         profile.bio = request.POST.get("bio")
#
#         user.save()
#         profile.save()
#
#         messages.success(request, "Profile updated successfully!")
#         return redirect('dashboard')
#
#     return render(request, 'Tedit-profile.html', {
#         'user': user,
#         'profile': profile
#     })
#
#
# # ---------------- CHANGE PASSWORD ---------------- #
#
# @login_required
# def change_password(request):
#     if request.method == "POST":
#         current = request.POST.get("current_password")
#         new = request.POST.get("new_password")
#         confirm = request.POST.get("confirm_password")
#
#         user = request.user
#
#         if not user.check_password(current):
#             messages.error(request, "Current password is incorrect")
#
#         elif new != confirm:
#             messages.error(request, "Passwords do not match")
#
#         elif len(new) < 6:
#             messages.error(request, "Password must be at least 6 characters")
#
#         else:
#             user.set_password(new)
#             user.save()
#             update_session_auth_hash(request, user)
#
#             messages.success(request, "Password updated successfully!")
#             return redirect('dashboard')
#
#     return render(request, 'Tchangepassword.html')
#
#
# # ---------------- SETTINGS ---------------- #
#
# @login_required
# def settings_page(request):
#     return render(request, 'Tsettings.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Profile


# ---------------- AUTH ---------------- #

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'Tsignup.html')   # ✅ fixed


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'Tlogin.html')   # ✅ fixed


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

from django.db.models import Count
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    category_filter = request.GET.get('category')

    # 🔥 ALL TASKS
    tasks = Task.objects.filter(user=request.user)

    print("Selected category:", category_filter)

    # 🔥 FILTER BY CATEGORY
    if category_filter:
        tasks = tasks.filter(category__iexact=category_filter)

    # 🔥 STATS
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()

    # 🔥 CATEGORY COUNT
    categories = Task.objects.filter(user=request.user)\
        .values('category')\
        .annotate(count=Count('id'))

    # ==============================
    # 🔔 REMINDER LOGIC
    # ==============================

    today = date.today()
    tomorrow = today + timedelta(days=1)

    reminder_tasks = Task.objects.filter(
        user=request.user,
        completed=False
    )

    # 🔥 FILTERS
    today_tasks = reminder_tasks.filter(deadline=today)
    tomorrow_tasks = reminder_tasks.filter(deadline=tomorrow)
    high_priority_tasks = reminder_tasks.filter(priority="High")

    # ==============================

    return render(request, 'Tindex.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
        'categories': categories,
        'selected_category': category_filter,

        # 🔥 NEW REMINDER DATA
        'today_tasks': today_tasks,
        'tomorrow_tasks': tomorrow_tasks,
        'high_priority_tasks': high_priority_tasks,
    })
# ---------------- DASHBOARD ---------------- #

from django.db.models import Count




# ---------------- ADD TASK ---------------- #

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        deadline = request.POST.get("deadline")
        priority = request.POST.get("priority")

        if not title or not description:
            messages.error(request, "All fields are required")
            return redirect('add_task')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            deadline=deadline if deadline else None,
            priority=priority
        )

        messages.success(request, "Task added successfully!")
        return redirect('dashboard')

    return render(request, 'Taddtask.html')   # ✅ fixed


# ---------------- COMPLETE TASK ---------------- #

@login_required
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('dashboard')


# ---------------- PROFILE ---------------- #

@login_required
def profile(request):
    return render(request, 'Tprofile.html', {   # ✅ fixed
        'user': request.user,
        'profile': request.user.profile
    })


# ---------------- EDIT PROFILE ---------------- #

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        new_username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        bio = request.POST.get("bio")

        # Validation
        if not new_username or not email:
            messages.error(request, "Username and Email are required")
            return redirect('edit_profile')

        if User.objects.exclude(id=user.id).filter(username=new_username).exists():
            messages.error(request, "Username already taken")
            return redirect('edit_profile')

        user.first_name = name
        user.email = email
        user.username = new_username
        profile.bio = bio

        user.save()
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')   # ✅ better UX

    return render(request, 'Tedit_profile.html', {   # ✅ FIXED NAME
        'user': user,
        'profile': profile
    })


# ---------------- CHANGE PASSWORD ---------------- #

@login_required
def change_password(request):
    if request.method == "POST":
        current = request.POST.get("current_password")
        new = request.POST.get("new_password")
        confirm = request.POST.get("confirm_password")

        user = request.user

        if not user.check_password(current):
            messages.error(request, "Current password is incorrect")

        elif new != confirm:
            messages.error(request, "Passwords do not match")

        elif len(new) < 6:
            messages.error(request, "Password must be at least 6 characters")

        else:
            user.set_password(new)
            user.save()
            update_session_auth_hash(request, user)

            messages.success(request, "Password updated successfully!")
            return redirect('dashboard')

    return render(request, 'Tchangepassword.html')   # ✅ fixed


# ---------------- SETTINGS ---------------- #

@login_required
def settings_page(request):
    return render(request, 'Tsettings.html')   # ✅ fixed
