# Views
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def joblistapi(request):
    job_list = Job.objects.all()
    data = JobSerializer(job_list, many=True).data
    return Response({'data':data})