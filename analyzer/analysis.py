from sklearn.cluster import KMeans
from scipy.stats import ttest_ind

def clustering(data, n_clusters=3):
 """
 Applies k-means clustering to identify cell populations.

 Parameters:
     data (pd.DataFrame): Preprocessed flow cytometry data.
     n_clusters (int): Number of clusters.

 Returns:
     np.ndarray: Cluster labels for each data point.
 """
 kmeans = KMeans(n_clusters=n_clusters)
 return kmeans.fit_predict(data)

def calculate_population_statistics(data, clusters):
    """
    Computes summary statistics for each marker within each cluster.
    """
    stats = {}
    for cluster_id in clusters['Cluster'].unique():
        cluster_data = data[clusters['Cluster'] == cluster_id]
        stats[cluster_id] = {
            'mean': cluster_data.mean().to_dict(),
            'std': cluster_data.std().to_dict(),
            'median': cluster_data.median().to_dict()
        }
    
    print("Calculated population statistics for each cluster.")
    return stats

def identify_outliers(data, threshold=3):
    """
    Identifies outliers based on a z-score threshold.
    """
    z_scores = (data - data.mean()) / data.std()
    outliers = (z_scores.abs() > threshold).any(axis=1)
    
    print(f"Identified {outliers.sum()} outliers based on threshold {threshold}.")
    return data[outliers]

def calculate_cluster_proportions(clusters):
    """
    Calculates the proportion of events in each cluster.
    """
    total = len(clusters)
    proportions = clusters['Cluster'].value_counts(normalize=True).to_dict()
    
    print("Calculated cluster proportions.")
    return proportions

def marker_pair_correlation(data, markers):
    """
    Computes the Pearson correlation coefficient between marker pairs.
    """
    correlations = data[markers].corr(method='pearson')
    print("Computed correlations between marker pairs.")
    return correlations
