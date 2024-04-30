from django.views.generic import CreateView, DetailView
from django.shortcuts import render, HttpResponse
from .models import UserActivity, ResizeImage
from .forms import ResizeImageForm
import cv2
from rembg import remove

class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "techno/index.html"


class ResultView(DetailView):
    model = UserActivity
    template_name = "techno/result.html"
    context_object_name = "user_activity"


def remove_background(source_image_path, destination_image_path):
    # try:
        with open(source_image_path, 'rb') as i, open(destination_image_path, 'wb') as o:
            # read source image in binary format
            input = i.read()
            # apply remove function to remove background
            output = remove(input)
            print(output, "OUTPUT")
            # save the new image in destination path
            o.write(output)
        print("Image background removed successfully")
    # except Exception as e:
    #     print(f"There is problem while processed -> {e}")


def resizeimage(request):
    if request.method == 'POST':  
        form = ResizeImageForm(request.POST, request.FILES)  
        if form.is_valid(): 
           image = request.FILES['image']
           print(image, "IMAGES")
           width = request.POST['width']
           height = request.POST['height']


           data = remove_background(image, "only-lion.jpg")
           return HttpResponse("Image background removed successfully!")
    
    else:  
        form = ResizeImageForm()  

    context = {
        'form': form
    }
    return render(request, 'techno/resize.html', context)





def remove_bg(request):
    # call function
    remove_background("images/back.jpg", "only-lion.jpeg")
    return HttpResponse("Image background removed successfully!")