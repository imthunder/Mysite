from django.shortcuts import render
from .models import DxIndex, DxList, DxDetail
from django.views.generic import ListView
import re

class IndexListView(ListView):
    queryset = DxIndex.objects.all()
    context_object_name = 'list'
    paginate_by = 12
    template_name = 'special/index.html'

def list_view(request, pid):
    list = DxList.objects.all().filter(pid = pid)
    topic = DxIndex.objects.get(id = pid)
    return render(request, 'special/list.html',{'list':list, 'topic':topic})

def detail_view(request, pid, detail_id):
    detail = DxDetail.objects.get(pid = detail_id)
    return render(request, 'special/detail.html',{'detail':detail})
