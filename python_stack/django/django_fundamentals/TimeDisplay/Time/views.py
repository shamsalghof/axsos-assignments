from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_time': now.strftime('%I:%M %p'),  # 11:26 AM
        'current_date': now.strftime('%b %d, %Y'),  # Oct 26, 2013
    }
    return render(request, 'index.html', context)