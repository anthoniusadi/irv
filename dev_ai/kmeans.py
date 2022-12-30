
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def cluster(x1,x2,k):
    data = list(zip(x1, x2))
    kmeans = KMeans(n_clusters = k, init = "k-means++", random_state = 42)
    y_kmeans = kmeans.fit(data)
    
    plt.scatter(x1, x2, c=y_kmeans.labels_) #type:ignore
    plt.xlabel('pc1')
    plt.ylabel('pc2')
    
    # plt.xlim([-5, 15])
    # plt.ylim([-5, 12])
    plt.show() 