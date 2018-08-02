from django.shortcuts import render

from django.http import HttpResponse
'''End Of Import'''
#---------------------------------------------------------------------#


# VIEW FUNCTIONS HERE!

#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def landing(request):
    return render(request, 'landingpage/land-page.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S HOME-PAGE
#################################################################################################################################################################################

#Passenger's HOME-PAGE view function
def passenger(request):
    return render(request, 'passenger/home.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S PROFILE-PAGE
#################################################################################################################################################################################

#PASSENGER'S PROFILE-PAGE view function

'''
 This page contains passengers info eg Name, Bio and useful information about driver
'''
def pprofile(request):
    return render(request, 'passenger/profile.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S  DESTINATION-PAGE
#################################################################################################################################################################################

#PASSENGER'S  DESTINATION-PAGE view function

'''
 This page enables passenger pick a destination point where they can be droped off
'''
def pdestination(request):
    return render(request, 'passenger/destination.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S  CONTACT-PAGE
#################################################################################################################################################################################

#PASSENGER'S  DESTINATION-PAGE view function

'''
 This page gives passenger contact info
'''
def pcontact(request):
    return render(request, 'passenger/contact.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  ABOUT-PAGE
#################################################################################################################################################################################

#ABOUT-INFO-PAGE

'''
 This page basically explains what the app is about
'''
def about(request):
    return render(request, 'uber/about.html')

#################################################################################################################################################################################