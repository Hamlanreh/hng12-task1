from django.http import JsonResponse
from django.utils.timezone import now

# Create your views here.

def public_api(request):
    data = {
        "email": "your-email@example.com",  # Replace with your HNG12 registered email
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"  # Replace with your repo URL
    }
    return JsonResponse(data)