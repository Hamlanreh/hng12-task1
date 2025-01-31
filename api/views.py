from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def public_api(request):
    data = {
        "email": "oluwabihammed49@example.com",
        "current_datetime": f"{datetime.now().isoformat()[:-3]}Z",
        "github_url": "https://github.com/Hamlanreh/hng12-task1"
    }
    return JsonResponse(data)