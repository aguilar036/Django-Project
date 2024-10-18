from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.forms import QuestionForm, ChoiceForm
from polls.models import Question, Choice


# Create your views here
def index(request):
    questions = Question.objects.order_by("-pub_date")[:10]
    context = {"questions": questions}

    return render(request, "polls/index.html", context)


def question_view(request):
    if request.method == "POST":
        choice_texts = request.POST.getlist('choice_text')
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()

            [Choice(question=question, choice_text=choice).save() for choice in choice_texts if len(choice) > 0]

            return render(request, "polls/success.html")

    question_form = QuestionForm()
    choice_forms = [ChoiceForm(prefix=str(i)) for i in range(1,4)]
    return render(request, 'polls/question_form.html', {'form': question_form, 'choice_forms': choice_forms})

def question_details(request, question_id: int):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/view.html", {"question": question})
