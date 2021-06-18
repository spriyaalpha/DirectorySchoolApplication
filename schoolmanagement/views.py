from django.shortcuts import render

import FinalUploadedDetails



def home_page(request):
    
    total_teacher= FinalUploadedDetails.models.UploadedPersonalDetails.objects.count()
  
    context = {
        
        'teacher': total_teacher,
        
    }
    return render(request, 'home.html', context)
