from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Advisor,Booking
from .serializers import *


# for getting all advisors
@api_view(['POST'])
def addAdvisor(request):
    if request.method == 'POST':
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                'message':'Advisor Added Successfully!',
            }
            return Response(response,status=status.HTTP_200_OK)

        else:
            response={
                    'message':'Advisor Adding Failed, Add All Parameters!',
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

# for registering users
@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = userRegisterSerilazer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response={
                'message':'Registered Successfully!',
                'user_id': user.id
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            response={
                'message':'Registration Failed, Add All Parameters!',
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

# for user login
@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        if email and password:
            try:
                user = User.objects.get(email = email)
                auth.login(request,user)
                response={
                    'message':'User Logged In Successfully!',
                    'user_id': user.id
                }
                return Response(response,status=status.HTTP_200_OK)

            except User.DoesNotExist:
                response={
                    'message':'User Does Not Exist!'
                }
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# for viewing all advisors
@api_view(['GET'])
def viewAdvisor(request,user_id):
    if request.method == 'GET':
        try:
            loggedInUser = User.objects.get(username = request.user)
            if request.user.is_authenticated:
                advisor = Advisor.objects.all()
                serializer = AdvisorSerializer(advisor,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                response ={
                     'message':'User Not Logged In, Login In and try to access again!'
                    }
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            response={
                'message':'User Does Not Exist, Enter Valid User Id In Parameter!'
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)
    else:
        return None

# for booking a call.
@api_view(['POST'])
def bookACall(request,user_id,advisor_id):
    if request.method == 'POST':
        try:
            advisor = Advisor.objects.get(id = advisor_id)
            try:
                user = User.objects.get(id = user_id)
                data = {
                    'user_id':user_id,
                    'advisor_id':advisor_id,
                    'time':request.data["time"]
                }
                serializer = bookingSerilazer(data = data)
                if serializer.is_valid():
                    user = serializer.save()
                    response={
                        'message':'Call Booked Successfully for user-id '+ str(user_id) + ' with advisor-id '+ str(advisor_id),
                    }
                    return Response(response,status=status.HTTP_200_OK)
                else:
                    response={
                        'message':'Call Booking Failed, Add All Parameters!',
                    }
                    return Response(response,status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                response = {
                    'message':'Invalid User ID!'
                }
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)

        except Advisor.DoesNotExist:
            response = {
                'message':'Invalid Advisor ID!'
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)

# for viewing all bookings.
@api_view(['GET'])
def viewBookings(request,user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id = user_id)
            bookings = list(Booking.objects.filter(user_id = str(user.id)))
            output = []
            i = 0
            # making list of dictonaries to display.
            while i < len(bookings):

                advisor = Advisor.objects.get(id = bookings[i].advisor_id_id)
                mydict={
                'Advisor Name': advisor.name,
                'Advisor Profile Pic Url': advisor.img_url,
                'Advisor id':advisor.id,
                'Booking Time':bookings[i].time,
                'Booking id':bookings[i].id,
                }
                output.append(mydict.copy())
                i = i+1

            return Response(output,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            response = {
                'message':'Invalid User ID!'
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)
    else:
        return None
