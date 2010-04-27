from django.template import RequestContext
from django.shortcuts import render_to_response

from karpelesbankruptcy.content.models import HomeText, AboutBankruptcyText, LoanModificationsText, AboutText, ResourcesText, ContactText, Chapter7Text, Chapter11Text, Chapter13Text, ReliefFromStayText, DisclaimerText

def index(request):
    """Submits the home page information to the URL
    """
    template = "index.html"
    homeText = HomeText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def about_bankruptcy(request):
    """Submits the about bankruptcy information to the URL
    """
    template = "about_bankruptcy.html"
    about_bankruptcy_text = AboutBankruptcyText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def loan_modifications(request):
    """Submits the loan modifications information to the URL
    """
    template = "loan_modifications.html"
    loan_modifications_text = LoanModificationsText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def about(request):
    """Submits the about information to the URL
    """
    template = "about.html"
    aboutText = AboutText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def resources(request):
    """Submits the resource text to the URL
    """
    template = "resources.html"
    resourceText = ResourcesText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def contact(request):
    """Submits the latest contact information to the URL
    """
    template = "contact.html"
    contactText = ContactText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def chapter_7(request):
    """Submits the latest chapter 7 information to the URL
    """
    template = "chapter_7.html"
    chapter_7_text = Chapter7Text.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def chapter_11(request):
    """Submits the latest chapter 11 information to the URL
    """
    template = "chapter_11.html"
    chapter_11_text = Chapter11Text.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def chapter_13(request):
    """Submits the latest chapter 13 information to the URL
    """
    template = "chapter_13.html"
    chapter_13_text = Chapter13Text.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def relief_from_stay(request):
    """Submits the latest relief from stay information to the URL
    """
    template = "relief_from_stay.html"
    relief_from_stay_text = ReliefFromStayText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def disclaimer(request):
    """ Submits latest disclaimer text to the URL
    """
    template = "disclaimer.html"
    disclaimerText=DisclaimerText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

