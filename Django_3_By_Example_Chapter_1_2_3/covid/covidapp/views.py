from django.shortcuts import render

# Create your views here.
import json
import requests

url = "https://rapidapi.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "2e7bfbf657msh4ead2fbb879faa0p15032djsnba33a57f3055"
    }

response = requests.request("GET", url, headers=headers).json()
data = response["results"]

def helloworldview(request):
    """
    string = "Everyone"
    contex = {'mylistitem': string}

    mylist = ['item1','item2','item3']
    contex = {'mylistitem': mylist}
    """
    numberofcountry = int(response["results"])
    mylist = []
    for x in range(0,numberofcountry):
        mylist.append(response["response"][x]["country"])
    mylist.sort()
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        #print(selectedcountry)
        for x in range(0,numberofcountry):
            if selectedcountry==response["response"][x]["country"]:
                new = response["response"][x]["cases"]["new"]
                active = response["response"][x]["cases"]["active"]
                critical = response["response"][x]["cases"]["critical"]
                recovered = response["response"][x]["cases"]["recovered"]
                total = response["response"][x]["cases"]["total"]
                death = int(total) - int(active) - int(recovered)
        contex = {'selectedcountry':selectedcountry,'mylist': mylist,'new':new, 'active':active,'critical':critical,'recovered':recovered,'total':total,'death':death}
        return render(request,'helloworld.html',contex)
    #print(response["response"][0])

    contex = {'mylist': mylist}

    return render(request, 'helloworld.html',contex)
