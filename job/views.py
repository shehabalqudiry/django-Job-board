from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            form = ApplyForm()
    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)


def add_job(request):
    if request.method == 'POST':
        form2 = JobForm(request.POST, request.FILES)
        if form2.is_valid:
            myform2 = form2.save(commit=False)
            myform2.owner = request.user
            myform2.save()
            return redirect(reverse())
    else:
        form2 = JobForm()

    context = {'job' : job_detail, 'form2':form2}
    return render(request, 'job/add_job.html',context)
