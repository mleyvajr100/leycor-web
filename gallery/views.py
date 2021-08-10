from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Furniture
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     return render(request, 'gallery/album.html', {})
#
# def test_view(request):
#     return render(request, 'gallery/work_test.html', {})

def gallery_view(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        furniture = Furniture.objects.filter(name__icontains=url_parameter)
    else:
        furniture = Furniture.objects.all()

    if request.is_ajax():
        html = render_to_string(
            template_name='gallery/single_element_disp.html',
            context={'furniture': furniture}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    ctx['furniture'] = furniture

    return render(request, 'gallery/album.html', context=ctx)
