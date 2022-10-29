import json
import logging

# Create your views here.
from django.http import JsonResponse

from .models import Question, Choice

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def index(request):
    """
    Function to print json response in postman
    """
    try:
        print(dir(request))
        # print(request.body)
        print(json.loads(request.body))
        # return HttpResponse("Hello, world. You're at the polls index.")
        return JsonResponse({"message": "Hello, world. You're at the polls index."}, status=201)
    except Exception as e:
        logging.error(e)


def create(request):
    """
    Function for creating request to perform create operation in Question model
    """
    try:
        sample = json.loads(request.body)
        if request.method == "POST":
            q = Question.objects.create(question_text=sample.get("question_text"))
            return JsonResponse({"Message": "Question created", "data": {"id": q.id, "question_text": q.question_text}},
                                status=201)
        return JsonResponse({"Message": "Method not allowed"},status=400)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status=400)


def update(request):
    """
    Function for creating request to perform update operation in Question model
    """
    try:
        obj = json.loads(request.body)
        if request.method == "PUT":
            id = obj.get("id")
            q = Question.objects.get(id=id)
            q.question_text = obj.get("question_text")
            q.save()
            return JsonResponse({"Message": "Question updated", "data": {"id": q.id, "question_text": q.question_text}},
                                status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status=400)


def get(request):
    """
    Function for creating request to get all data from Question model
    """
    try:
        if request.method == "GET":
            samp = Question.objects.all()
            return JsonResponse({"Message": "Questions all data are",
                                 "data": [{"id": q.id, "question": q.question_text} for q in samp]}, status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status=400)


def delete(request):
    """
    Function for creating request to delete data of Question model
    """
    try:
        obj1 = json.loads(request.body)
        if request.method == "DELETE":
            id = obj1.get("id")
            Question.objects.get(id=id).delete()
            return JsonResponse({"Message": "Question deleted"}, status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status=400)


def create_choice(request):
    """
    Function for creating request for create operation using Choice model
    """
    try:
        obj = json.loads(request.body)
        if request.method == "POST":
            id = obj.get('id')
            q= Question.objects.get(pk=id)
            choice = q.choice_set.create(choice_text=obj.get("choice_text"), votes=0)
            return JsonResponse({"Message": "Choice created", "data": {"id": choice.id, "choice_text": choice.choice_text}},
                                status=201)
        return JsonResponse({"Message": "Method not allowed"}, status=204)

    except Exception as e:
        return JsonResponse({"message": str(e), }, status= 400)


def get_choice(request):
    """
    Function for creating request to get all data from Choice model
    """
    try:
        obj = json.loads(request.body)
        if request.method == "GET":
            id = obj.get('id')
            q = Question.objects.get(pk=id)
            c = q.choice_set.all()
            return JsonResponse({"Message": "Questions all data are","data":[{"id": choice.id, "choice": choice.choice_text} for  choice in c]}, status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status= 400)

def update_choice(request):
    """
    Function for creating request to perform update operation in Choice model
    """
    try:
        obj = json.loads(request.body)
        print(request.method)
        if request.method == "PUT":
            id = obj.get("id")
            q = Choice.objects.get(pk=id)
            q.choice_text = obj.get("choice_text")
            q.save()
            return JsonResponse({"Message": "Question updated", "data": {"id": q.id, "question_text": q.choice_text}},
                                status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status= 400)


def delete_choice(request):
    """
    Function for creating request to delete data of Question model
    """
    try:
        obj1 = json.loads(request.body)
        if request.method == "DELETE":
            id = obj1.get("id")
            Choice.objects.get(pk=id).delete()
            return JsonResponse({"Message": "Choice deleted"}, status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        return JsonResponse({"message": str(e), }, status=400)

