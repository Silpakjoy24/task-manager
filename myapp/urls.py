from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # ---------------- DASHBOARD ---------------- #
    path('', views.dashboard, name='dashboard'),

    # ---------------- AUTH ---------------- #
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ---------------- TASK ---------------- #
    path('add-task/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.mark_completed, name='mark_completed'),

    # ---------------- PROFILE ---------------- #
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # ---------------- PASSWORD ---------------- #
    path('change-password/', views.change_password, name='change_password'),

    # 🔥 FORGOT PASSWORD (FIX YOUR ERROR)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Tforgotpassword.html'), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # ---------------- SETTINGS ---------------- #
    path('settings/', views.settings_page, name='settings'),
]



