from .models import *

def contact_info(request):
    contacts = ContactInformation.objects.first()
    return {'contacts':contacts}

def social_links(request):
    socials = SocialAccount.objects.all()[:4]
    return {'socials':socials}