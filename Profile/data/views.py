from django.shortcuts import render, redirect
from django.http import request, response
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from .models import Project, Education, Certification, Company
import os

# Create your views here.
def index_Page(request):
    project_yes = Project.objects.filter(project_upload_to_youtube='Yes')
    project_no = Project.objects.filter(project_upload_to_youtube='No')
    company = Company.objects.all()

    education = Education.objects.all()
    certifications = Certification.objects.all()
    print(education.reverse())
    # # print(project)
    # return render(request,"indexPage.html",{'parameter':project})
    return render(request, 'Main.html',
                  {'project_yes': project_yes, 'education': education, 'certifications': certifications,
                   "project_no": project_no, "company": company})


def show_project(request, pk):
    parameter = Project.objects.get(id=pk)
    parameter = Project.objects.filter(project_name=parameter)
    print("---lhu-", parameter)
    if request.method == 'POST':
        return redirect('/')

    return render(request, 'edit.html', {'parameter': parameter})


def download_pdf(request):
    print('----------------------------', os.getcwd()+'/static/assets/uploads')


    file_path = os.getcwd()+'/static/assets/uploads/Resume.pdf'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse ('GHHHHHHHHHH')
    # raise Http404
