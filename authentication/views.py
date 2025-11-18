from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse(
                {
                    "username": user.username,
                    "status": True,
                    "message": "Login successful!",
                },
                status=200,
            )
        return JsonResponse(
            {
                "status": False,
                "message": "Login failed, account is disabled.",
            },
            status=401,
        )

    return JsonResponse(
        {
            "status": False,
            "message": "Login failed, please check your username or password.",
        },
        status=401,
    )

