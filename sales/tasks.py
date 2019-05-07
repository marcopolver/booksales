from background_task import background
from sales import models
import numpy as np
from kmeans.kmeans_functions import elbow_kmeans


@background(schedule=60)
def generate_clusters():

    print('Working')

    #Get all the students
    students = models.Student.objects.all()

    students_pts = np.array()

    for student in students:

        wishes = student.wishlist_books
        int_titles = student.interesting_titles

        #fis, mat, inf, mec, en, eco, aut, sta
        values = [0,0,0,0,0,0,0,0]

        #Scansione libri in wishlist
        for wish in wishes.all():
            if wish.ad_id.title_isbn.category == 'FIS':
                values[0] = values[0] + 1
            elif wish.ad_id.title_isbn.category == 'MAT':
                values[1] = values[1] + 1
            elif wish.ad_id.title_isbn.category == 'INF':
                values[2] = values[2] + 1
            elif wish.ad_id.title_isbn.category == 'MEC':
                values[3] = values[3] + 1
            elif wish.ad_id.title_isbn.category == 'EN':
                values[4] = values[4] + 1
            elif wish.ad_id.title_isbn.category == 'ECO':
                values[5] = values[5] + 1
            elif wish.ad_id.title_isbn.category == 'AUT':
                values[6] = values[6] + 1
            elif wish.ad_id.title_isbn.category == 'STA':
                values[7] = values[7] + 1

        #Scansione titoli d'interesse
        for title in int_titles.all():
            if title.title_isbn.category == 'FIS':
                values[0] = values[0] + 5
            elif title.title_isbn.category == 'MAT':
                values[1] = values[1] + 5
            elif title.title_isbn.category == 'INF':
                values[2] = values[2] + 5
            elif title.title_isbn.category == 'MEC':
                values[3] = values[3] + 5
            elif title.title_isbn.category == 'EN':
                values[4] = values[4] + 5
            elif title.title_isbn.category == 'ECO':
                values[5] = values[5] + 5
            elif title.title_isbn.category == 'AUT':
                values[6] = values[6] + 5
            elif title.title_isbn.category == 'STA':
                values[7] = values[7] + 5

        #Creazione del punto nell'iperpiano
        students_pts = np.append(students_pts, values)

        #Esecuzione algoritmo kmeans
        clusters, _, k = elbow_kmeans(students_pts, 12)

        for i in range(len(clusters)):

            students[i].cluster = clusters[i]
            students[i].save()