from django.shortcuts import render
from summe_app.models import File
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from summe_app.forms import UploadFileForm
from summe_app.models import UploadFile
from summe_app.models import GetText
from summe_app.forms import GetTextForm
import requests
from bs4 import BeautifulSoup


# Create your views here.


def index(request):
    return render(request, "index.html")


def index_3(request):
    return render(request, "index3.html")


def index_2(request):
    return render(request, "index2.html")


def index_4(request):
    return render(request, "index4.html")


def dummy(request):
    return render(request, "dummy.html")


def uploadFile(request):
	if request.method == "POST":
		File(textFile=request.POST['title']).save()
		return render(request,"index2.html", {"message":"Successfully summarized!"})
	else:
		return render(request,"index.html",{"message": ""})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFile(docfile=request.FILES['docfile'])
            instance.save()
            return HttpResponse("uploaded %s" % request.FILES['docfile'])
    else:
        form = UploadFileForm()

    '''NO NEED, DUMMY LANG TONG BABA. TEST
    args = {}
    args.update(csrf(request))

    args['form'] = form
    '''

    return render(request, 'index2.html')


def get_text(request):
    if request.method == 'POST':
        form = GetTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            print(text)
            return HttpResponse("success")
    else:
        return HttpResponse("fail")


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'sampleText.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for parag in soup.findAll('p', {'class': 'first'}):
            justin = parag.get('p')
            print(justin)


'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['title'])
        return HttpResponse("uploaded %s"%request.FILES['title'])
    else:
        form = UploadFileForm()
        return render(request, 'index3.html', {'form': form})

def handle_uploaded_file(f):
    import datetime as dt
    from summe_project import settings
    now = dt.datetime.now()
    with open("%s\\%s%s%s%s%s%s_%s"%(settings.MEDIA_ROOT, now.year, now.month, now.day, now.hour, now.minute, now.second, f), 'w+') as destination:
        print(f.readlines())
        destination.writelines(f.readlines())
'''

'''
new
'''
'''

def get_text_form(request):
    if request.method == 'POST':
        form = (request.POST, request.FILES)
        handle_get_text_form(request.FILES['texttext'])
        return HttpResponse("uploaded file")
    else:
        form = UploadFileForm()
        return render(request, 'index3.html', {'form': form})


def handle_get_text_form(g):

    from summe_project import settings
    form = cgi.FieldStorage()
    with open('fileToWrite.txt' % settings.MEDIA_ROOT, 'w+') as fileOutput:
        fileOutput.write(form.getValue('texttext'))
'''