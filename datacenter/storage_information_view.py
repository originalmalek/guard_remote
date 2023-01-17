import  datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .format_duration import format_duration, get_duration

def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visits = Visit.objects.filter(leaved_at=None)

    for not_leaved_visit in not_leaved_visits:
        user_name = not_leaved_visit.passcard.owner_name
        entered_time = localtime(not_leaved_visit.entered_at)
        now = localtime(datetime.datetime.now(datetime.timezone.utc))
        visit_duration = get_duration(entered_time, now)
        non_closed_visits.append({
                'who_entered': user_name,
                'entered_at': entered_time,
                'duration': format_duration(visit_duration),
            })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
