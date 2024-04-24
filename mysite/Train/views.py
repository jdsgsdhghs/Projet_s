from django.shortcuts import render, get_object_or_404
from Train.models import Trainsncf

# Create your views here.
def index(request):
    all_trains = Trainsncf.objects.all()
    return render(request, "Train/index.html", {"trains": all_trains})

    trajet_one = Trainsncf.objects.get(TrainID = 1)
    # pour afficher un fichier  de html
    return render(request, "Train/index.html", {
      "id": trajet_one.TrainID,
       "city":  trajet_one.City,
       "depart": trajet_one.Departure_Time,
       "arrivee": trajet_one.Arrival_Time,
    })


def show(request, train_id):
    myTrain = Trainsncf.objects.get(TrainID = train_id)

    return render(request, "Train/show.html", {
        "numero": myTrain.TrainID,
        "ville" : myTrain.City,
        "depart" : myTrain.Departure_Time,
        "arrivé" : myTrain.Arrival_Time,
        "precedent" : int(train_id) - 1,
        "suivant" : int(train_id) + 1,
    })

def random(request) : 
    # On crée une fonction aléatoire
    def random_fonction():
        import random
        # On génère un id aléatoire entre 0 et 21
        id_random = random.randint(0,21)
        return id_random

    
    train_alea = random_fonction()

    trajetaleatoire = Trainsncf.objects.get(TrainID = train_alea)


    return render(request, 'Train/random.html', {
       "numero": trajetaleatoire.TrainID,
       "ville": trajetaleatoire.City,
       "depart": trajetaleatoire.Departure_Time,
       "arrivé": trajetaleatoire.Arrival_Time,
    })
