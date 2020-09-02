# Create your views here.
import requests

from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import JsonResponse

from myapi.models import Launch
from .serializers import LaunchSerializer


class LaunchesListView(ListAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class LaunchDetailView(RetrieveAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


def next_launch(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        json = r.json()
        myapi = Launch()

        myapi.launch_year = int(json['launch_year'])
        myapi.launch_date_utc = json['launch_date_utc']
        myapi.launch_date_local = json['launch_date_local']
        myapi.rocket_id = json['rocket']['rocket_id']
        myapi.rocket_name = json['rocket']['rocket_name']
        myapi.rocket_type = json['rocket']['rocket_type']
        myapi.land_success = 'False'
        myapi.site_name = json['launch_site']['site_name_long']
        myapi.customer = json['rocket']['second_stage']['payloads'][0]['customers'][0]
        myapi.nationality = json['rocket']['second_stage']['payloads'][0]['nationality']
        myapi.launch_success = 'False'

        serializer = LaunchSerializer(data=myapi.as_json())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def latest_launch(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        json = r.json()
        myapi = Launch()
        myapi.launch_year = int(json['launch_year'])
        myapi.launch_date_utc = json['launch_date_utc']
        myapi.launch_date_local = json['launch_date_local']
        myapi.rocket_id = json['rocket']['rocket_id']
        myapi.rocket_name = json['rocket']['rocket_name']
        myapi.rocket_type = json['rocket']['rocket_type']
        myapi.land_success = 'False'
        myapi.site_name = json['launch_site']['site_name_long']
        myapi.customer = json['rocket']['second_stage']['payloads'][0]['customers'][0]
        myapi.nationality = json['rocket']['second_stage']['payloads'][0]['nationality']
        myapi.launch_success = 'False'

        serializer = LaunchSerializer(data=myapi.as_json())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def upcoming_launches(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        json = r.json()

        launches = []

        for element in json:
            myapi = Launch()
    
            myapi.launch_year = int(element['launch_year'])
            myapi.launch_date_utc = element['launch_date_utc']
            myapi.launch_date_local = element['launch_date_local']
            myapi.rocket_id = element['rocket']['rocket_id']
            myapi.rocket_name = element['rocket']['rocket_name']
            myapi.rocket_type = element['rocket']['rocket_type']
            myapi.land_success = 'False'
            myapi.site_name = element['launch_site']['site_name_long']
            myapi.customer = element['rocket']['second_stage']['payloads'][0]['customers']
            myapi.nationality = element['rocket']['second_stage']['payloads'][0]['nationality']
            myapi.launch_success = 'False'

            launches.append(myapi.as_json())
            serializer = LaunchSerializer(data=myapi.as_json())
            if serializer.is_valid():
                serializer.save()

        return JsonResponse(launches, safe=False, status=201)


def past_launches(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/past')
        json = r.json()

        launches = [{ }]

        for element in json:
            myapi = Launch()
            
            myapi.launch_year = int(element['launch_year'])
            myapi.launch_date_utc = element['launch_date_utc']
            myapi.launch_date_local = element['launch_date_local']
            myapi.rocket_id = element['rocket']['rocket_id']
            myapi.rocket_name = element['rocket']['rocket_name']
            myapi.rocket_type = element['rocket']['rocket_type']
            myapi.land_success = 'False'
            myapi.site_name = element['launch_site']['site_name_long']
            myapi.customer = element['rocket']['second_stage']['payloads'][0]['customers']
            myapi.nationality = element['rocket']['second_stage']['payloads'][0]['nationality']
            myapi.launch_success = 'False'

            launches.append(myapi.as_json())
            serializer = LaunchSerializer(data=myapi.as_json())
            if serializer.is_valid():
                serializer.save()

        return JsonResponse(launches, safe=False, status=201)
