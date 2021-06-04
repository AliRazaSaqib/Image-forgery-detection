from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
# from .forms import HotelForm, Hotel
# from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from check import detect
# from django.http import HttpResponseRedirect, HttpResponse
from .forms import HotelForm
from .models import Hotel

global Path
Path = "http://127.0.0.1:8887/templates/images/forPreview.png"
global statement
statement = "Button is clicked"


def home(request):
    # if request.POST.get('second_click'):
    if request.method == "POST":
        form = HotelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'home.html', {'obj': obj})
    else:
        form = HotelForm()
    return render(request, 'home.html', {'form': form})


def process(request):
    if request.method == "POST":
        print(12)
        value = request.POST['hotel_Main_Img']
        print(13)
        value2 = request.POST['get_block_size']
        print(value2)
        value3 = int(value2)
        print(value3)

        file = "D://Final Year project material//Coding//correct code//NewFile//imageChecker//templates//images//" + value
        # global Path
        image_name = detect.detect(file,
                                   "D://Final Year project material//Coding//correct code//NewFile//imageChecker//templates//images//result//",
                                   value3)
        global Path
        Path = "http://127.0.0.1:8887/templates/images/result/" + image_name
    return render(request, 'process.html')


def help(request):
    return render(request, 'help.html')  # It will render the help module


def delete(request, id):
    obj = Hotel.objects.get(id=id)
    obj.delete()
    return redirect('/ImagePreview')


def ImagePreview(request):
    get_img = Hotel.objects.all()
    return render(request, 'history.html', {'fetch_images': get_img})


def edit(request, id):
    get_img = Hotel.objects.get(id=id)
    return render(request, 'edit.html', {'get_img': get_img})


def update(request, id):
    get_img = Hotel.objects.get(id=id)
    form = HotelForm(data=request.POST, files=request.FILES, instance=get_img)
    form.save()
    obj = form.instance
    return render(request, 'edit.html', {'obj': obj})


def search(request):
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     posts = Hotel.objects.filter(name__icontains=q)
    # else:
    #     posts = Hotel.objects.all()
    given_name = request.get['q']
    get_img = Hotel.objects.filter(name=given_name)
    return render(request, 'history.html', {'get_img': get_img})


def final(request):
    print(Path)
    get_pt = Path
    return render(request, 'final.html', {'get_pt': get_pt})  # It will render the finale reuslt module


def accuracy(request):
    if request.POST.get('mask1'):
        print("first button is clicked")
    if request.POST.get('maks2'):
        print("second button is clicked")
    return render(request, 'Accuracy.html')
