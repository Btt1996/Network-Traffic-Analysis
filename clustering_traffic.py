import pandas as pd
from sklearn.cluster import KMeans

def cluster_traffic(data):
    # Prepare data for clustering
    X = data[['column1', 'column2', 'column3']]

    # cluster data using k-means
    kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
    labels = kmeans.labels_
    num_clusters = len(set(labels))

    # Add labels to the data
    data['cluster'] = labels

    # Save the results to csv
    data.to_csv("clustered_traffic.csv", index=False)
    return num_clusters

if __name__ == "__main__":
    # load traffic data
    data = pd.read_csv("traffic_data.csv")

    # cluster traffic data
    num_clusters = cluster_traffic(data)
    print("Number of clusters: ", num_clusters)
