from .models import Appointment


def patient_message_counter(request):
    unread_patient_message_count = 0

    if request.user.is_authenticated and hasattr(request.user, 'patient'):
        unread_patient_message_count = (
            Appointment.objects.filter(
                patient=request.user.patient,
                patient_message_seen=False
            )
            .exclude(receptionist_message__isnull=True)
            .exclude(receptionist_message='')
            .count()
        )

    return {
        'unread_patient_message_count': unread_patient_message_count
    }