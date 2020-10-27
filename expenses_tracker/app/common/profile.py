from app.models import Profile


def get_profile():
    return Profile.objects.first()
