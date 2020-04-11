from django.shortcuts import render
from .models import destination
# Create your views here.

def index(request):
    dest1=destination()
    dest1.name="jeypore"
    dest1.desc="City of Koraput"
    dest1.img="destination_2.jpg"
    dest1.price=1234
    dest1.offer=False

    dest2=destination()
    dest2.name="koraput"
    dest2.desc="dist Koraput"
    dest2.img="destination_3.jpg"
    dest2.price=12345
    dest2.offer=True

    dest3=destination()
    dest3.name="bariniput"
    dest3.desc="our native"
    dest3.img="destination_4.jpg"
    dest3.price=1234567
    dest3.offer=False

    dest4=destination()
    dest4.name="jeypore"
    dest4.desc="City of Koraput"
    dest4.img="destination_2.jpg"
    dest4.price=1234
    dest4.offer=False

    dest5=destination()
    dest5.name="koraput"
    dest5.desc="dist Koraput"
    dest5.img="destination_3.jpg"
    dest5.price=12345
    dest5.offer=False
    
    dest6=destination()
    dest6.name="bariniput"
    dest6.desc="our native"
    dest6.img="destination_4.jpg"
    dest6.price=1234567
    dest6.offer=False

    dest7=destination()
    dest7.name="jeypore"
    dest7.desc="City of Koraput"
    dest7.img="destination_2.jpg"
    dest7.price=1234
    dest7.offer=False

    dest8=destination()
    dest8.name="koraput"
    dest8.desc="dist Koraput"
    dest8.img="destination_3.jpg"
    dest8.price=12345
    dest8.offer=False
    
    dest9=destination()
    dest9.name="bariniput"
    dest9.desc="our native"
    dest9.img="destination_4.jpg"
    dest9.price=1234567
    dest9.offer=False

    dests =[dest1,dest2,dest3,dest4,dest5,dest6,dest7,dest8,dest9]

    return render(request,'index.html',{'dests':dests})