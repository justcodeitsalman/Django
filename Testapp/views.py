from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os
from Testapp.models import Gym_Member


#Create your views here.

def Hello_World_Fun(request):
    date={'date': str(Current_date_time()), 'hostname': Host_Details(),'name':'salman','rollno':'3','marks':'100','list':[10,20,30,40]}
    response= render(request,'Testapp/home.html',context=date)
    return response

def Current_date_time():
    now = str(datetime.now().year)
    return now

def Host_Details():
    hostname=os.uname()[1]
    return hostname

def Return_data(request):
    query_opt=Gym_Member.objects.all()

    return render(request,'Testapp/table.html',{'opt':query_opt})

def main(request):
    dict={}
    return render(request,"Testapp/main.html",dict)

def Login(request):
    dict={}
    return render(request,"Testapp/login.html",dict)

def join(request):
    dict={}
    return render(request,"Testapp/join.html",dict)

def register(request):
    dict={}
    return render(request,"Testapp/regform.html",dict)

def event(request):
    dict={}
    return render(request,"Testapp/events.html",dict)

from django.views.generic import View
import boto3
import os 

bucket = "vmax-vedio-library"

class upload(View):
     def upload_file(self,file_name, bucket):
        object_name = file_name
        s3_client = boto3.client('s3')
        response = s3_client.upload_file(file_name, bucket, object_name)
        if response==200:
            dict=self.show_image(bucket)
        
        return dict
        
     def post(self,request,*argv,**kargv):
         f=request.POST['file']
         path=os.path.join("/Users/salmandesai/Python/Django-Project/firstProject/static/S3upload/", f)
         dict=self.upload_file(path, bucket)
         return render(request,"Testapp/events.html",dict) 

    
     def show_image(self,bucket):
        s3_client = boto3.client('s3')
        public_urls = []
        try:
            for item in s3_client.list_objects(Bucket=bucket)['Contents']:
                presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
                public_urls.append(presigned_url)
        except Exception as e:
            pass
        # print("[INFO] : The contents inside show_image = ", public_urls)
        return public_urls
    

