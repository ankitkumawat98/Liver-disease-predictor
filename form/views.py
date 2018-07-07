from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import  numpy as np

def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return (1/(1+np.exp(-x)))

def predict(data):
    Q = np.array([[-1.18333468,-0.16221422,-2.40907575,-4.26540043,-3.02030764,-3.16714497,-1.1685135,-1.10858509, 1.53156496, 1.12853328]])
    x = np.array([[float(data["age"])/90,float(data["gender"]),float(data["tot_bilirubin"])/75,float(data["direct_bilirubin"])/19.7,float(data["alkphos"])/2110,float(data["sgpt"])/2000,float(data["sgot"])/4929,float(data["tot_proteins"])/9.6,float(data["albumin"])/5.5,float(data["ag_ratio"])/2.8,]])
    return sigmoid(np.dot(x,Q.T))[0][0]

def index(request):
    check = "";
    if request.method=="POST":
        check = "Result: \n"
        data = request.POST
        p = predict(request.POST)
        if(p>=0.5):
            check +="\tThe patient doesn't have any liver disease.\n"
        else:
            check +="The patient may have a liver disease.\n The probability of it is "+str(1-p)

    template = loader.get_template("form/index.html")
    return HttpResponse(template.render({"check":check},request))
