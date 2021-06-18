import csv,io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonalInfoForm
from .models import PersonalInfoNew
from FinalUploadedDetails.models import UploadedPersonalDetails
# Create your views here.

def load_upazilla(request):
    district_id = request.GET.get('district')
    upazilla = Upazilla.objects.filter(district_id=district_id).order_by('name')

    upazilla_id = request.GET.get('upazilla')
    union = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    context = {
        'upazilla': upazilla,
        'union': union
    }
    return render(request, 'others/upazilla_dropdown_list_options.html', context)
@login_required(login_url='login')
def teacher_registration(request):
    form = PersonalInfoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form=PersonalInfoForm()
        obj = PersonalInfoNew.objects.get(activated=False)
        
        with open(obj.File.path,'r') as f:
            reader= csv.reader(f)
            for i,row in enumerate(reader):
                if i==0:
                    pass
                else:                    
                    UploadedPersonalDetails.objects.get_or_create(
                        FirstName=row[0],
                        LastName=row[1],
                        Photo=row[2],
                        PhoneNumber=row[3],
                        EmailAddress=row[4],
                        RoomNumber=row[5],
                        SubjectsTaught=row[6],
                    )   
                    
            obj.activated= True
            obj.save()
    return render(request, 'teacher/teacher-registration.html', {'form':form})
def teacher_list_sort(request):
    UploadedDetailSort=UploadedPersonalDetails.objects.all().order_by('LastName')   
    return render(request, 'teacher/teacher-list-sort.html', {'UploadedDetailSort': UploadedDetailSort})
    
def teacher_list(request):
    UploadedDetails = UploadedPersonalDetails.objects.all()
    return render(request, 'teacher/teacher-list.html', {'UploadedDetails': UploadedDetails})

def teacher_profile(request, FinalUploadedDetails_id):    
    UploadedDetailsnew = UploadedPersonalDetails.objects.get(id=FinalUploadedDetails_id)     
    return render(request, 'teacher/teacher-profile.html', {'UploadedDetailsnew': UploadedDetailsnew})


#@permission_required('sivapriya.abc123')

    