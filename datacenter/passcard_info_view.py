import  datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .format_duration import format_duration, get_duration


def is_strange_visit(visit_duration):
    return visit_duration / 60 > 1000


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = []
    user_visits = Visit.objects.filter(passcard=passcard)

    for user_visit in user_visits:
        entered_time = user_visit.entered_at
        leaved_time = user_visit.leaved_at
        if leaved_time == None:
            leaved_time = datetime.datetime.now(datetime.timezone.utc)
        visit_duration = get_duration(entered_time, leaved_time)

        is_strange = is_strange_visit(visit_duration)

        passcard_visits.append({
                                    'entered_at': entered_time,
                                    'duration': format_duration(visit_duration),
                                    'is_strange': is_strange
                                    })
    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)
