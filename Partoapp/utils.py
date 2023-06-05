import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph= base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph




def get_plot(x,y,x1,y1,x2,y2):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('Partograph')
    #plt.tight_layout()
    plt.xlim(0, 12)
    plt.ylim(0,10)
    plt.xlabel('Hours')
    plt.ylabel('Cervical Dilation (cm)')
    plt.title('Partogram')
    plt.grid(True)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.yticks([1,2,3,4,5,6,7,8,9,10])
    plt.plot(x1,y1,x2,y2)
    plt.scatter(x,y)
    graph=get_graph()
    return graph


def get_plot1(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(9,6))
    plt.title('Partograph')
    #plt.tight_layout()
    plt.xlim(0, 12)
    plt.ylim(80,200)
    plt.yticks([80,90,100,110,120,130,140,150,160,170,180,190,200])
    plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12])
    plt.xlabel('Hours')
    plt.ylabel('FHR (in bpm)')
    plt.title('Fetal Heart Rate')
    plt.grid(True)
    plt.plot(x,y)
    graph=get_graph()
    return graph