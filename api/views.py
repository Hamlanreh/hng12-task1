from django.http import JsonResponse
from django.utils.timezone import now

# Create your views here.

def public_api(request):
    data = {
        "email": "oluwabihammed49@example.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/Hamlanreh/hng12-task1"
    }
    return JsonResponse(data)