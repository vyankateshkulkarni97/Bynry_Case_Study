from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CapturedData

@csrf_exempt
def capture_data(request):
    if request.method == 'POST':
        # Assuming 'data' field contains either screenshot or screen recording file
        data = request.FILES.get('data')
        
        # Save data to database
        captured_data = CapturedData(data=data)
        captured_data.save()

        return JsonResponse({'message': 'Data captured and saved successfully.'}, status=200)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
