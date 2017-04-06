#!/usr/bin/python3
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail
from .forms import ContactForm, EstateForm
from .models import Immobilie, ImmoNews, Contact, Leistungen
from securemail.models import SaveContact
import os
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
import mimetypes
import urllib


def home(request):
    news = ImmoNews.objects.filter(is_active=True).order_by('-created')
    estates = Immobilie.objects.all().exclude(immobilienArt='VK').order_by('-created')[:3]
    contact = Contact.objects.all()
    context = {
        'news': news,
        'estates': estates,
        'contact': contact
    }
    return render(request, 'index.html', context)


def person(request):
    leistung = Leistungen.objects.filter(art='PE')
    contact = Contact.objects.all()
    context = {
        'leistung': leistung,
        'contact': contact
    }
    return render(request, 'leistung.html', context)


def sell(request):
    leistung = Leistungen.objects.filter(art='VK')
    contact = Contact.objects.all()
    context = {
        'leistung': leistung,
        'contact': contact
    }
    return render(request, 'leistung.html', context)


def buy(request):
    leistung = Leistungen.objects.filter(art='AK')
    contact = Contact.objects.all()
    context = {
        'leistung': leistung,
        'contact': contact
    }
    return render(request, 'leistung.html', context)


def rating(request):
    leistung = Leistungen.objects.filter(art='BW')
    contact = Contact.objects.all()
    context = {
        'leistung': leistung,
        'contact': contact
    }
    return render(request, 'leistung.html', context)


def consulting(request):
    leistung = Leistungen.objects.filter(art='BR')
    contact = Contact.objects.all()
    context = {
        'leistung': leistung,
        'contact': contact
    }
    return render(request, 'leistung.html', context)

############
#Immobilien#
############
def one(request):
    estates = Immobilie.objects.filter(immobilienArt='EFH').order_by('wohnfl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def eigen(request):
    estates = Immobilie.objects.filter(immobilienArt='WE').order_by('wohnfl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def kapital(request):
    estates = Immobilie.objects.filter(immobilienArt='WK').order_by('wohnfl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def more(request):
    estates = Immobilie.objects.filter(immobilienArt='MFH').order_by('wohnfl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def plot(request):
    estates = Immobilie.objects.filter(immobilienArt='GR').order_by('grundstuecksfl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def business(request):
    estates = Immobilie.objects.filter(immobilienArt='GEW').order_by('gewerbefl')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def sold(request):
    estates = Immobilie.objects.filter(immobilienArt='VK').order_by('kfpreis')
    contact = Contact.objects.all()
    context = {
        'estates': estates,
        'contact': contact
    }
    return render(request, 'estate.html', context)


def contact(request):
    form_class = ContactForm
    contact = Contact.objects.all()
    context = {
        'form': form_class,
        'contact': contact
    }

    return render(request, 'contact.html', context)


def impressum(request):
    contact = Contact.objects.all()
    context = {
        'contact': contact,
    }
    return render(request, 'impressum.html', context)


def datenschutz(request):
    return render(request, 'impressum.html')


def agb(request):
    return render(request, 'impressum.html')


def geldwaesche(request):
    return render(request, 'impressum.html')


def verbraucherinfo(request):
    return render(request, 'impressum.html')


def estateDetail(request, estatename):
    estate = Immobilie.objects.filter(title=estatename).prefetch_related('energieAusweis', 'objekbesrbng')
    form_class = EstateForm
    contact = Contact.objects.all()
    context = {
        'estate': estate,
        'form': form_class,
        'contact': contact
    }
    return render(request, 'estateDetail.html', context)


def special(request, estatename, specialname):
    estate = Immobilie.objects.filter(title=estatename).prefetch_related('bild')
    special = specialname
    contact = Contact.objects.all()
    form_class = EstateForm

    context = {
        'estate': estate,
        'form': form_class,
        'contact': contact,
        'special': special
    }
    return render(request, 'special.html', context)


def specialv(request, estatename, specialname):
    estate = Immobilie.objects.filter(title=estatename).prefetch_related('video')
    special = specialname
    contact = Contact.objects.all()
    form_class = EstateForm

    context = {
        'estate': estate,
        'form': form_class,
        'contact': contact,
        'special': special
    }
    return render(request, 'special.html', context)


def specialg(request, estatename, specialname):
    estate = Immobilie.objects.filter(title=estatename).prefetch_related('grdriss')
    special = specialname
    contact = Contact.objects.all()
    form_class = EstateForm

    context = {
        'estate': estate,
        'form': form_class,
        'contact': contact,
        'special': special
    }
    return render(request, 'special.html', context)


def danke(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_anliegen = request.POST.get(
                'contact_anliegen'
                ,'' )
            contact_gender = request.POST.get(
                'contact_gender'
                , '')
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_gender': contact_gender,
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            send_mail(
                'Grund: '+contact_anliegen,
                content,
                contact_email,
                ['info@witza-immobilien.de'],
                fail_silently=False,
            )

            savecon = SaveContact()
            savecon.name = contact_name
            savecon.mail = contact_email
            savecon.save()
            return render(request, 'danke.html', context)

    return HttpResponseRedirect('/contact')


def thanks(request):
    form_class = EstateForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_anliegen = request.POST.get(
                'contact_anliegen'
                ,'' )
            contact_gender = request.POST.get(
                'contact_gender'
                , '')
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            estate = request.POST.get('estate', '')

            # Email the profile with the
            # contact information
            template = get_template('estate_template.txt')
            context = Context({
                'contact_gender': contact_gender,
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_anliegen': contact_anliegen,
                'form_content': form_content,
            })
            content = template.render(context)

            send_mail(
                'ID: '+estate,
                content,
                contact_email,
                ['info@witza-immobilien.de'],
                fail_silently=False,
            )

            savecon = SaveContact()
            savecon.name = contact_name
            savecon.mail = contact_email
            savecon.save()
            return render(request, 'danke.html', context)

    return HttpResponseRedirect('/contact')



def output(request):
    return redirect("https://google.com/")


def expose(request, filename):
        file_path = filename
        original_filename = filename
        fp = open(file_path, 'rb')
        response = HttpResponse(fp.read())
        fp.close()
        type, encoding = mimetypes.guess_type(original_filename)
        if type is None:
            type = 'application/octet-stream'
        response['Content-Type'] = type
        response['Content-Length'] = str(os.stat(file_path).st_size)
        if encoding is not None:
            response['Content-Encoding'] = encoding

        # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
        if u'WebKit' in request.META['HTTP_USER_AGENT']:
            # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
            filename_header = 'filename=%s' % original_filename.encode('utf-8')
        elif u'MSIE' in request.META['HTTP_USER_AGENT']:
            # IE does not support internationalized filename at all.
            # It can only recognize internationalized URL, so we do the trick via routing rules.
            filename_header = ''
        else:
            # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
            filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
        response['Content-Disposition'] = 'attachment; ' + filename
        return response
