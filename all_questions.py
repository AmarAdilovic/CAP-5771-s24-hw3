# Add import files
import pickle



# -----------------------------------------------------------
# Agglomerative hierarchical clustering refers to procedures such as single link, complete link, and group average,
# while k-means clustering refers to k-means with random initialization of centroids and Euclidean distance.
def question1():
    answers = {}

    # Text-book notes (Chapter 5):
    # K-Means
        #  Defines a prototype in terms of a centroid (usually the mean of a group of points)
            # Doesn't need to be an actual data point
        # Algorithm
            # Choose K initial centroids, where K is user specified, each point is assigned to the nearest centroid
                # Recompute the centroid until the centroids stop changing
                # Collection of points assigned to a centroid is a cluster
                # Most of the convergence happens in early steps, usually can repeat until a certain weak condition is met
                    # Such as until only 1% of points change clusters 
                # Object function - measures the quality of the clustering
                    # Sum of Squared Error (SSE)
                        # Prefer the K-means run with the smallest SSE,
                        # as this means they are more representative of the points in the cluster
        # Between Group Sum of Squares (SSB)
            # The sum of the squared distance of a cluster centroid to the overall mean of all the data points
                # The higher the total SSB of a clustering - the more seperated the clusters are from one another
        # Cohesion
            # Maximizing the similarity of the points in a cluster to the cluster centroid
            # Calculated like SSE, but instead of using distance use cosine similarity
        # Cohesion and Seperation
            # Strong relationship between cohesion and seperation
                # Minimizing SSE (cohesion) is equivalent to maximizing SSB (separation)
            # It is possible to show that the sum of the total SSE and the total SSB is a constant;
            # i.e., that it is equal to the total sum of squares (TSS), which is the sum of squares of the distance of each point to
            # the overall mean of the data
        # K-Means++
            # Guaranteed to find a K-Means clustering solution that is optimal within Olog(k)
                # Results in better clustering results in terms of lower SSE
        # Issues
            # Outliers
                # When the squared error criterion is used - outliers can have a large influence. 
                # When outliers are present, resulting prototypes are not representative.
                    # Can identify and remove outliers ahead of time in acceptable applications, eliminate small clusters,
                    # or eliminate points with unusually high SSE contributions
        # Time/Space Complexity
            # Space
                # O((m + K)n), m: num points, n: num attributes
            # Time
                # O(I×K×m×n), I: num iterations for convergence
    # K-Medoid
        # Defines a prototype in terms of a medoid (the most representative point for a group of points)
        # Medoid by definition must be an actual data point
    # Agglomerative Hierarchical Clustering
        # Agglomerative
            # Start with points as individual clusters, each step merge the closest pair of clusters.
                # Need to define cluster proximity
            # Often displayed using a tree-like diagram called a dendrogram
        # Divisive
            # Start with one all inclusive-cluster, each step split a cluster until only clusters composing one points remain.
                # Need to determine which cluster to split and how to
        # Issues
            # Outliers
                # Large impact on Ward's method and centroid-based hierarchical clustering approaches
                    # These approaches increase SSE and distort centroids
                # Single-link, complete-link, and group average - outliers are less problematic
                    # Can discard signleton or small clusters to remove outliers
        # Time/Space Complexity
            # O(m^2), where m is the number of data points
    # --------- Question A ---------
    # Agglomerative hierarchical clustering procedures are better able to handle outliers than k-means
    
    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Outliers have a larger impact in K-Means as the mere precence of outliers results in K-Means producing non-representative prototypes, and handling the outliers either requires pre-processing or post-processing the points or clusters. With agglomerative hierarchical clustering, single-link, complete-link, and group average cluster proximity measures are more resistant to outliers."

    # --------- Question B ---------
    # For any given data set, different runs of k-means can produce different clusterings,
    # but agglomerative hierarchical clustering procedures will always produce the same clustering

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "With K-Means the K initial clusters are chosen randomly, introducing randomness and thus variation. With Agglomerative hierarchical clustering, if the linkage criterion is consistent, the clusters are defined in an objective and consistent manner, with little room for randomness and thus variation."

    # --------- Question C ---------
    # K-means take less time and memory than agglomerative hierarchical clustering
    # and is the most efficient clustering algorithm possible.

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-Means is not the most efficient clustering algorithm possible, that will depend on the data set size, shape, and many other factors."

    # --------- Question D ---------
    # During a post-processing step for K-means, a cluster is split by picking one of the points of
    # the cluster as a new centroid and then reassigning the points in the cluster either to the original
    # centroid or the new centroid. What happens to the SSE of the clustering?

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The SSE will decrease, as one of the points of the cluster is selected as a new centroid, the points will point to whichever centroid is closer, reducing the overall distance for the points to their centroids and thus reducing SSE."

    # --------- Question E ---------
    # When clustering a dataset using K-means, whenever SSE decreases, cohesion increases.

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "When SSE decreases, the average distance between the points and the centroid decreases, in turn meaning the similarity of those points to the centroid has increased, thus meaning that cluster cohesion has increased."

    # --------- Question F ---------
    # When clustering a dataset using K-means, whenever SSB (the between sum of squares) increases, separation increases.

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "By definition, the higher the total SSB of a clustering - the more seperated the clusters are from one another."

    # --------- Question G ---------
    # Cohesion and separation are independent for K-Means,
    # i.e., improving cohesion (smaller SSE) doesnt necessarily improve separation (larger between sum of squares (SSB)).

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "There is a strong relationship between cohesion and seperation, minimizing SSE (cohesion) is equivalent to maximizing SSB (separation)."

    # --------- Question H ---------
    # When clustering a dataset using K-means, SSE + BSS is a constant.

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "There is a proof to prove the Total Sum of Squares (TSS) can be proven to be equal to constants SSE and SSB/BSS."

    # --------- Question I ---------
    # When clustering a dataset using K-means, whenever cohesion increases, separation increases.

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Decreasing SSE (cohesion) is equivalent to increasing SSB (separation)."

    return answers


# -----------------------------------------------------------
# Note that we are referring to the very basic k-means algorithm presented and not bisecting k-means or k-means++.
# Note that for all three figures, the initial centroids are given by the symbol: For figures (a) and (b),
# assume the shaded areas represent points with the same uniform density. For Figure (c), the data
# points are given as red dots, and their values are indicated under the dots. No explanation for
# your answer is necessary unless you feel there is some ambiguity in the figure or the question.
def question2():
    answers = {}

    # --------- Question A ---------
    # For Figure (a) and the given initial centroid: When the k-means algorithm completes,
    # each shaded circle will have one cluster centroid at its center.
    
    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Due to the large separation between the two circles, the iterative recomputation of the centroids will occur until the centroid stops changing, which will happen at the center of the two clusters."

    # --------- Question B ---------
    # For Figure (b) and the given initial centroids:
    # When the k-means algorithms completes,
    # there will be one cluster centroid in the center of each of the two shaded regions,
    # and each of the two final clusters will consist only of points from one of the shaded regions.
    # In other words, none of the two final clusters will have points from both shaded regions.

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to the crescent shapes of the shaded regions, the proximity of the points to the centroid will necessitate that the final clusters will have points from both shaded regions."

    # --------- Question C ---------
    # For Figure (c) and the given initial centroids, the final clustering for k-means contains an empty cluster.
    
    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The computation of the centroids will result in the centroid at 12.5 being empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = 7.5

    # type: a string that evaluates to a float
    answers["(b) SSE"] = 7.5

    # type: a string that evaluates to a float
    answers["(c) SSE"] = 7.5

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 0

    # type: int
    answers["(a) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: int
    answers["(b) Circle (a)"] = 0

    # type: int
    answers["(b) Circle (b)"] = 0

    # type: int
    answers["(b) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set()

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: set
    answers["(b)"] = set()

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set()

    # type: set
    answers["(a) boundary"] = set()

    # type: set
    answers["(a) noise"] = set()

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = ""

    # type: string
    answers["(b) Row 2"] = ""

    # type: string
    answers["(b) Row 3"] = ""

    # type: string
    answers["(b) Row 4"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = []

    # type: list
    answers["(b)"] = []

    # type: list
    answers["(c)"] = []

    # type: list
    answers["(d)"] = []

    # type: list
    answers["(e)"] = []

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = ""

    # type: string
    answers["(a) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = ""

    # type: string
    answers["(b) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
