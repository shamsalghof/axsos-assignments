from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Book
from django.http import JsonResponse
import json


def index(request):
    """Display login/registration page"""
    if 'user_id' in request.session:
        return redirect('dashboard')
    return render(request, 'login_reg.html')


def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
            'confirm_pw': request.POST.get('confirm_pw', ''),
            'birthday': request.POST.get('birthday', ''),
        }

        result = User.objects.create_user(data)

        if result['success']:
            user = result['user']
            request.session['user_id'] = user.id
            request.session['user_name'] = user.get_full_name()
            messages.success(request, f'Successfully registered!')
            return redirect('dashboard')
        else:
            for field, error in result['errors'].items():
                messages.error(request, error)
            return render(request, 'login_reg.html', {
                'old_data': data,
                'errors': result['errors']
            })

    return redirect('index')


def login(request):
    """Handle user login"""
    if request.method == 'POST':
        data = {
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', '')
        }

        errors = User.objects.login_validator(data)

        if errors:
            for field, error in errors.items():
                messages.error(request, error)
            return render(request, 'login_reg.html', {
                'login_errors': errors,
                'login_data': data
            })

        user = User.objects.get(email=data['email'])
        request.session['user_id'] = user.id
        request.session['user_name'] = user.get_full_name()
        messages.success(request, f'Successfully logged in!')
        return redirect('dashboard')

    return redirect('index')


def dashboard(request):
    """Display success page (session protected)"""
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('index')

    books = Book.objects.all()
    try:
        user = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        request.session.flush()
        return redirect('index')

    context = {
        'user': user,
        'user_name': request.session.get('user_name', ''),
        'books': books
    }
    return render(request, 'dashboard.html', context)


def logout(request):
    """Handle user logout"""
    request.session.flush()
    messages.success(request, 'Successfully logged out!')
    return redirect('index')


def check_email_ajax(request):
    """Check if email is unique via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', '').strip().lower()

            if not email:
                return JsonResponse({'available': False, 'message': 'Email is required'})

            if User.objects.filter(email=email).exists():
                return JsonResponse({'available': False, 'message': 'Email already in use'})
            else:
                return JsonResponse({'available': True, 'message': 'Email is available'})
        except:
            return JsonResponse({'error': 'Invalid request'})

    return JsonResponse({'error': 'Method not allowed'})


def create_book(request):
    if request.method == "POST":
        postData = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
        }
        errors = Book.objects.basic_validator(postData)
        user = User.objects.get(id=request.session['user_id'])

        if errors:
            for value in errors.values():
                messages.error(request, value, extra_tags='book')
            return redirect('dashboard')
        else:
            book = Book.objects.create(
                title=request.POST.get('title'),
                description =request.POST.get('description'),
                uploaded_by=user,
            )
            book.users_who_like.add(user)
            return redirect('dashboard')
    return redirect('dashboard')

def book_info(request,book_id):

    book = Book.objects.get(id=book_id)
    context = {
        'book' : book,
        'user': User.objects.get(id=request.session['user_id']),

    }
    return render(request,'book_info.html',context=context)


def update_book(request, book_id):
    # Must be logged in
    if 'user_id' not in request.session:
        return redirect('index')

    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return redirect('dashboard')

        # Only the uploader can update their own book
        if book.uploaded_by != user:
            messages.error(request, "You can only edit books you uploaded", extra_tags='book')
            return redirect('book_info', book_id=book_id)

        # Validate the submitted data
        postData = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
        }
        errors = Book.objects.basic_validator(postData)

        if errors:
            for value in errors.values():
                messages.error(request, value, extra_tags='book')
            return redirect('book_info', book_id=book_id)

        # Apply the changes
        book.title = postData['title'].strip()
        book.description = postData['description'].strip()
        book.save()   # updated_at refreshes automatically (auto_now=True)

    return redirect('book_info', book_id=book_id)

def delete_book(request, book_id):
    # Must be logged in
    if 'user_id' not in request.session:
        return redirect('index')

    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.get(id=book_id)

        # Only the uploader can delete their own book
        if book.uploaded_by == user:
            book.delete()
        else:
            messages.error(request, "You can only delete books you uploaded", extra_tags='book')

    return redirect('dashboard')

def favorite_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(user)
    return redirect('book_info', book_id=book_id)


def unfavorite_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.remove(user)
    return redirect('book_info', book_id=book_id)