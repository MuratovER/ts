import os
import matplotlib.pyplot as plt
import numpy as np

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = '/home/ilya/projects/topskills/ts/mainsite/static/mainsite/images/wheeloflife/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt))
    os.chdir(pwd)
    plt.close()

# rcParams['font.family'] = 'fantasy'
# rcParams['font.fantasy'] = 'Arial'




def getImageSkills(values):
    # VALUES внутренний мир. карьера (учеба). здоровье. отношения

    # values = [9, 6, 9 , 8]

    fig = plt.figure(figsize = [5,5])

    plt.plot([10, 10], [0, 20], color = 'b')
    plt.plot([0, 20], [10, 10], color = 'b')

    graph1 = plt.plot(
                    [10 - values[0], 10             , 10 + values[2],               10, 10 - values[0]], 
                    [10            , 10 + values[1], 10             , 10 - values[3],                     10],  "o-")



    

    plt.text(-2, 7, 'Внутренний мир', rotation=90)
    plt.text(7, 22, 'карьера')
    plt.text(21, 10, 'Здоровье', rotation=270)
    plt.text(7, -1, 'Отношения')

    plt.axis('off')
    name = ""
    for elem in values:
        name += str(elem)
    save(name=name, fmt='png')
    # plt.show()
    # name = "mainsite/images/wheeloflife/png/9698.png"
    # name = "mainsite/images/wheeloflife/png/{}.png".format(name)
    return name