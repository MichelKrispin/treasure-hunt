import random

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .forms import StageForm
from .models import Map, Stage

# One of these are randomly selected
errors = [
    'Nicht ganz',
    'Nicht wirklich',
    'Versuch es doch einmal nochmal',
    'Näää',
    'Knapp. Glaub ich.',
    'Nicht mal nah dran',
    'So kurz davor',
    'Achso? Das war ja nicht so wirklich richtig...',
    'Uff...',
    'Äh nein?',
    'Was war denn das für eine schräge Idee?',
    'Ganz sicher nicht...',
    'Pffffffff.',
    'Nö',
    'Einfach nur falsch.',
    'Leider nicht',
    'Hehe. Ne.',
]


class IndexView(generic.ListView):
    template_name = 'hunting/index.html'
    model = Map
    context_object_name = 'maps'


class StageView(generic.DetailView):
    template_name = 'hunting/stage.html'
    Model = Stage

    def get_object(self, queryset=None):
        return Stage.objects.get(slug=self.kwargs.get('id'))


def check_answer(correct_answer, given_answer):
    """ Checks whether the given answer matches the correct answer. """
    # First lower everything
    correct_answer = correct_answer.lower()
    given_answer = given_answer.lower()

    # If the length of the string is only one (one word or one number)
    # just compare them
    space_splitted_correct_answer = correct_answer.split(' ')
    dot_splitted_correct_answer = correct_answer.split('.')
    if (len(space_splitted_correct_answer) == 1 and 
        len(dot_splitted_correct_answer) == 1 ):
        return correct_answer == given_answer

    # Otherwise if there are multiple words check whether each
    # is also contained in the given answer
    len_space_splitted_correct_answer = len(space_splitted_correct_answer)
    if len_space_splitted_correct_answer > 1:
        num_correct = 0
        for parts in space_splitted_correct_answer:
            if '.' in parts: # If dot inside remove
                parts = parts.replace('.', '')
            if parts in given_answer:
                num_correct += 1
        # If there are as many correct elements as elements in the answer its correct
        return num_correct == len_space_splitted_correct_answer

    # If there are no spaces but dots it is probably a date
    len_dot_splitted_correct_answer = len(dot_splitted_correct_answer)
    if len_dot_splitted_correct_answer > 1:
        num_correct = 0
        for parts in dot_splitted_correct_answer:
            if parts in given_answer:
                num_correct += 1
        # If there are as many correct elements as elements in the answer its correct
        return num_correct == len_dot_splitted_correct_answer

    # If nothing happend? No idea
    return False

def check_stage(request, id):
    stage = get_object_or_404(Stage, pk=id)
    
    # This here is the answer checking thing
    if check_answer(stage.answer, request.POST['answer']):
        return HttpResponseRedirect(reverse('stage', args=(stage.next_stage.slug,)))
    return render(request, 'hunting/stage.html', { 'stage': stage, 'error': random.choice(errors) })

