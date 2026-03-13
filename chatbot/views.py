from django.shortcuts import render
from django.http import JsonResponse
from patientsNew.models import Patient
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot_ai import hospital_chat

def chat_page(request):
    return render(request, "chatbot/chat.html")

def chat_with_ai_page(request):
    return render(request, "chatbot/chatwithai.html")

def chat_api(request):

    message = request.GET.get("message")

    # simple search
    patients = Patient.objects.filter(name__icontains=message)

    if patients.exists():
        data = []
        for p in patients:
            data.append({
                "name": p.name,
                "age": p.age,
                "diagnosis": p.diagnosis,
                "doctor": p.doctor,
                "room": p.room
            })

        return JsonResponse({"reply": data})

    # search diagnosis
    patients = Patient.objects.filter(diagnosis__icontains=message)

    if patients.exists():
        names = [p.name for p in patients]

        return JsonResponse({
            "reply": f"Patients with {message}: {', '.join(names)}"
        })

    return JsonResponse({"reply": "No patient found"})

@csrf_exempt
def chat_api_with_ai(request):

    if request.method == "POST":

        data = json.loads(request.body)

        message = data.get("message")

        reply = hospital_chat(message)

        return JsonResponse({"reply": reply})