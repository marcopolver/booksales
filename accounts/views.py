from django.shortcuts import render, HttpResponseRedirect
from sales.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from sales import models
from datetime import datetime
import numpy as np
from kmeans.kmeans_functions import elbow_kmeans


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

'''
Function that finds the suggested ads for the student
'''
def find_ads(current):
    # Cluster number of the current student
    c_number = current.user.cluster.cluster_number

    # Students of the same cluster
    same_cluster_entries = models.Cluster.objects.filter(cluster_number=c_number)
    similar_students = [entry.student for entry in same_cluster_entries]

    # Lists for similar students' interesting titles and wishlist books
    int_titles = {}
    wish_ads = {}

    for student in similar_students:

        wishes = student.wishlist_books.all()
        interests = student.interesting_titles.all()

        # Inserimento wishes
        # if(wishes.count() != 0):
        for wish in wishes:

            if wish in wish_ads.keys():
                wish_ads[wish] += 1
            else:
                wish_ads[wish] = 1

        # Inserimento interests
        for interest in interests:

            if interest in int_titles.keys():
                int_titles[interest] += 1
            else:
                int_titles[interest] = 1

def evaluate_students():

    #Students list
    students = models.StudentProfile.objects.all()

    #Array of interesting data about the students
    students_data = np.array()
    #TODO: Vai avanti


def first_page(request, username):
    #User who is entering the page
    current = get_object_or_404(models.StudentProfile, username=username)

    #If true the algorhitm has to be run, otherwise we can directly access data about the last built clusters
    needs_run = False

    #Get info about the previous clustering algorithm runs
    clustering_runs = models.ClusteringInfo.objects.all()

    #If the clustering algorithm has never been run, then run it
    if(clustering_runs.count() == 0):
        needs_run = True
    #If the last execution of the algorithm was more than 1h ago, then run the algorithm
    elif((datetime.now()-clustering_runs.latest().run_time)>3600):
        needs_run = True

    #If it's not needed to run the algorithm, we check the current Cluster value for the student
    if(not needs_run):

        #Cluster number of the current student
        c_number = current.user.cluster.cluster_number

        #Students of the same cluster
        same_cluster_entries = models.Cluster.objects.filter(cluster_number=c_number)
        similar_students = [entry.student for entry in same_cluster_entries]

        #Lists for similar students' interesting titles and wishlist books
        int_titles = {}
        wish_ads = {}

        for student in similar_students:

            wishes = student.wishlist_books.all()
            interests = student.interesting_titles.all()

            #Wishes selection
            #if(wishes.count() != 0):
            for wish in wishes:

                if wish in wish_ads.keys():
                    wish_ads[wish] += 1
                else:
                    wish_ads[wish] = 1

            #Interests selection
            for interest in interests:

                if interest in int_titles.keys():
                    int_titles[interest] += 1
                else:
                    int_titles[interest] = 1

        #Wishes and interests sorting
        ordered_wishes = list(sorted(wishes, key=wishes.__getitem__, reverse=True))
        ordered_interests = list(sorted(interests, key=interests.__getitem__, reverse=True))

        #Wishes and interests mix
        final_wishes = []

        #For the first 10 interests, the first ad is chosen
        int_wishes_count = 0
        for i in range(min(10, len(ordered_interests))):
            final_wishes.append(ordered_interests[i].title_isbn.annunci_titolo.first())
            int_wishes_count += 1
        for j in range(min(20-int_wishes_count, len(ordered_wishes))):
            final_wishes.append(ordered_wishes[j])

        #TODO: Visualizzazione risultati

    #Elbow k-means
    else:

        elbow_kmeans()





