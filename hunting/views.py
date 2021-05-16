import random
from fuzzywuzzy import fuzz

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Map, Stage

# One of these are randomly selected
errors = {
    'close': [
        'Nicht ganz',
        'Knapp. Glaub ich.',
        'So kurz davor',
        'Uff...',
        'Ganz knappes Ding',
        'Wirkling eng',
        'Naja fast',
        'Noch n bisschen',
        'Du kannst es fast riechen',
        'So nah, dass ein Schritt zurück vielleicht helfen kann',
    ],
    'far': [
        'Nicht wirklich',
        'Näää',
        'Nicht mal nah dran',
        'Einfach nur falsch.',
        'Pffffffff sicher nicht.',
        'Was war denn das für eine schräge Idee?',
        'Ganz sicher nicht...',
        'Ei ei ei...',
        'Na klar.',
        'Sowas abwegiges',
        'An sowas hätte ich im Leben nicht gedacht',
        'Da muss ich drüber nachdenken... Nein.',
        'Ha ne',
        'O ___ O',
    ],
    'always': [
        'Versuch es doch einfach nochmal',
        'Achso? Das war ja nicht so wirklich richtig...',
        'Nö',
        'Leider nicht',
        'Hehe. Ne.',
        'Äh nein?',
        'Bestimmt nicht',
    ]
}


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

    # Now get the difference
    try:
        answer_ratio = fuzz.token_sort_ratio(correct_answer, given_answer)
    except Exception as e:
        print(f'Error with fuzzywuzzy ({correct_answer}, {given_answer})\n{e}')

    # Then give a correct answer depending on the correctness
    if answer_ratio > 95: # Above 95 is correct
        return 'correct'

    # 50 Percent Chance to get a always possible answer
    if random.choice([True, False]):
        return 'always'

    if answer_ratio > 60: # Quite close
        return 'close'

    return 'far' # Otherweise its far away

def check_stage(request, id):
    current_stage = get_object_or_404(Stage, pk=id)

    # This here is the answer checking thing
    answer_type = check_answer(current_stage.answer, request.POST['answer'])
    if answer_type == 'correct':
        # If the answer is correct get the stage with the next higher level
        next_stage = Stage.objects.filter(level__gt=current_stage.level).first()
        return HttpResponseRedirect(reverse('stage', args=(next_stage.slug,)))

    # If the answer was wrong just return a random error and the same stage again
    return render(request, 'hunting/stage.html', { 'stage': current_stage, 'error': random.choice(errors[answer_type]) })

