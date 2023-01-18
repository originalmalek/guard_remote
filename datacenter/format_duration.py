from django.utils.timezone import localtime

def get_duration(entered_time, leaved_time):
    total_visit_time = localtime(leaved_time) - localtime(entered_time)
    total_visit_time_in_seconds = round(total_visit_time.total_seconds())
    return total_visit_time_in_seconds


def format_time(duration_hours, duration_minutes, duration_seconds):
    if duration_hours < 10:
        duration_hours = '0' + str(duration_hours)
    if duration_minutes < 10:
        duration_minutes = '0' + str(duration_minutes)
    if duration_seconds < 10:
        duration_seconds = '0' + str(duration_seconds)
    return duration_hours, duration_minutes, duration_seconds

def format_duration(visit_duration):
    duration_hours = visit_duration // 3600
    duration_minutes = (visit_duration % 3600) // 60
    duration_seconds = (visit_duration % 3600 % 60) // 60
    duration_hours, duration_minutes, duration_seconds = format_time(duration_hours, duration_minutes,
                                                                     duration_seconds)

    return f'{duration_hours} часов {duration_minutes} минут {duration_seconds} секунд'
