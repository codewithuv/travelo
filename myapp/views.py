from django.shortcuts import render
from .models import Destination
def index(request):
    dests=Destination.objects.all()
    
    return render (request,'index.html', {'dests' :dests})
#     dest1= Destination()
#     dest1.name ="Mumbai"
#     dest1.desc ="The city that never sleep"
#     dest1.price =700
#     dest1.img = "destination_8.jpg"
#    # return render (request,'index.html', {'dest1' :dest1})

#     dest2= Destination()
#     dest2.name ="Bengaluru"
#     dest2.desc ="The city of India"
#     dest2.price =750
#     dest2.img = "destination_9.jpg"
#     #return render (request,'index.html', {'dest1' :dest1})

#     dest3= Destination()
#     dest3.name ="Hydrabad"
#     dest3.desc ="The city of Birayani"
#     dest3.price =400
#     dest3.img = "destination_1.jpg"
#     dest3.offer =True
#     dests=[dest1, dest2, dest3]

