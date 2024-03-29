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
# Consider the four data points shown in the following Figure. The distance between each data point to the center C is R.
def question3():
    answers = {}

    # sum of the squared error (SSE)
        # calculate the error of each data point, i.e., its Euclidean distance to the closest centroid,
        # and then compute the total sum of the squared errors

    # --------- Question A ---------
    # Compute the total SSE of the data points to the centroid, C.
    
    # SSE = 4 x R^2

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 x R^2"

    # --------- Question B ---------
    # Compute the total SSE of the data points to the origin, O.

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 x R^2"

    # --------- Question C ---------
    # Using parts (a) and (b),
    # compute the SSE for the 8 data points shown below with respect to the centroid, D.
    # Note that points u, v, w, and x lie on a circle of radius R/2.
    # Also, the figure is symmetric with respect to the horizontal line running through D
    
    # type: a string that evaluates to a float
    answers["(c) SSE"] = "8 x (R^2)((R / 2)^2)"

    return answers

# 


# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 0

    # type: int
    answers["(a) Circle (c)"] = 3

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Due to the large number of points in C and as each circle is equidistant, the centroids centralizing in C will decrease SSE the most amount and would thus converge there."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 0

    # type: int
    answers["(b) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to the large number of points in C, as the centroids move around B, they will be drawn and move to C, however as the centroid in A has no reason to move to B, it will stay in A."

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroids in C will not move away due to the distances involved, however the centroid in A will stay in A as it would capture the points in cluster B."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # MIN / Single-Link
        # the proximity of two clusters is defined as the minimum of the distance between any two points in the two different clusters.
    # MAX / Complete-Link
        # the proximity of two clusters is defined as the maximum of the distance between any two points in the two different clusters.
    
    # Question A
    # Using the single link (MIN) hierarchical clustering technique, which pair of groups would you consider for merging?
    
    # type: set
    answers["(a)"] = {
        'Group A',
        'Group B'
    }

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The minimum distance between any two points in two different clusters are the farthest-right point in group A, and the farthest-left point in group B."

    # Question B
    # Using the complete link (MAX) hierarchical clustering technique, which pair of groups would you consider for merging? 
    
    # type: set
    answers["(b)"] = {
        'Group C',
        'Group B'
    }

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The maximum distance between any two points in two different clusters are the farthest-left point in group C, and the farthest-right point in group B."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # DBSCAN
        # Density
            # Center-based approach
                # Density is estimated for a particular point by counting the number of points within a specified radius, Eps.
                    # This includes the point itself.
        # Core points
            # A point is a core point if there are at least MinPts within a distance of Eps,
            # where MinPts and Eps are user-specified parameters.
        # Border points
            # Not a core point, but falls in the neighborhood of a core point
        # Noise points
            # Neither a core or border point
        # Algorithm
            # Label all points as core, border, or noise
            # Elimate noise points
            # Put an edge between all core points within a distance - Eps - of each other
            # Make each group of connected core points into a separate cluster
            # Assign each border point to one of the clusters of its associated core points

    # A point is a core point if its density (number of points within epsilon) is ≥ MinPts.
    # Given that MinPts = 3 and EPS = 1, answer the following questions.

    # Density when epsilon = 1
        # A = 1
            # 1 ≥ 3 === False
        # B = 3
            # 3 ≥ 3 === True (Core)
        # C = 4
            # 4 ≥ 3 === True (Core)
        # D = 2
            # 2 ≥ 3 === False
        # E = 3
            # 3 ≥ 3 === True (Core)
        # F = 4
            # 4 ≥ 3 === True (Core)
        # G = 2
            # 2 ≥ 3 === False
        # H = 1
            # 1 ≥ 3 === False
        # I = 3
            # 3 ≥ 3 === True (Core)
        # J = 3
            # 3 ≥ 3 === True (Core)
        # L = 3
            # 3 ≥ 3 === True (Core)
        # M = 3 
            # 3 ≥ 3 === True (Core)

    # Density when epsilon = √2
        # A = 2
        # B = 5
        # C = 5
        # D = 3
        # E = 6
        # F = 5
        # G = 3
        # H = 2
        # I = 5
        # J = 4
        # L = 4
        # M = 4 

    # type: set
    answers["(a) core"] = {
        'B',
        'C',
        'E',
        'F',
        'I',
        'J',
        'L',
        'M'
    }

    # type: set
    answers["(a) boundary"] = {
        'D',
        'G'
    }

    # type: set
    answers["(a) noise"] = {
        'A',
        'H'
    }

    # type: set
    answers["(b) cluster 1"] = {
        'B',
        'C',
        'D',
        'E',
        'F',
        'G'
    }

    # type: set
    answers["(b) cluster 2"] = {
        'I',
        'J',
        'L',
        'M'
    }

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'I',
        'J',
        'L',
        'M'
    }

    # type: set
    answers["(c)-a boundary"] = {
        'A',
        'H'
    }

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G'
    }

    # type: set
    answers["(c)-b cluster 2"] = {
        'H',
        'I',
        'J',
        'L',
        'M'
    }

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # Entropy
        # Measures how well cluster labels match externally supplied class labels
        # The degree to which each cluster consists of objects of a single class.
            # Smaller = less disorder
            # Higher = more disorder

    # Which cluster has the largest clustering entropy?

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "This cluster has the most uniform distribution across the different classes/categories."

    # Which cluster has the smallest clustering entropy?

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "This cluster has the highest homogeneity due to the Water category dominating the other categories."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # In theory, if we have well-separated clusters, then the
    # similarity matrix should be roughly block-diagonal. If not, then the patterns
    # displayed in the similarity matrix can reveal the relationships between clusters.

    # Match the distance matrices (Matrix 1, Matrix 2, Matrix 3) with the sets of points (Dataset X, Dataset Y, and Dataset Z).

    # type: string
    # Matrix 2 === Dataset X as the highest distances (red blocks) are mirrored from one another
    # Matrix 1 === Dataset Z as the red blocks are more pronounced than in Matrix 3
    # (Dataset X, Matrix 2), (Dataset Z, Matrix 1), (Dataset Y, Matrix 3)
    answers["(a) Matrix 1"] = "Dataset Z"

    # Provide a brief explanation of the diagaonal entries and the non-diagonal entries.

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The diagonal entries represent well-separated, compact clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The non-diagonal entries represent the relationship between the clusters. In this case, the light green/yellow blocks are on the same axis but opposite ends, while the red blocks are the compact clusters that are furthest from one another."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The diagonal entries represent well-separated clusters. There is a mixture of compactness, thus the first and last diagonal blocks are less blue than the two middle ones which are a deeper blue due to being more compact."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "The light green/yellow blocks represent clusters that are moving diagonally and the light-red blocks are the non-compact clusters that are on opposite diagonal ends of one another."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The diagonal entries represent well-separated clusters. There is a mixture of compactness, thus the first and last diagonal blocks are less blue than the two middle ones which are a deeper blue due to being more compact."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In this case, the light green/yellow blocks are on the same axis but opposite ends thus the differences in intensity, while the red blocks are the clusters that are furthest from one another."

    # For the symmetric matrix given in Matrix 2 match the four rows to the corresponding clusters
    # (characterized the nearest alphabet in each cluster (e.g: A, B, C, D))
    # in the dataset that you match with it in the previous question

    # (Row 1, A), (Row 2, B), (Row 3, C), (Row 4, D)

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Cluster A is the furthest from cluster D, Row 1 shows a match on the first cluster, while being the opposite of the last cluster block, this can only be cluster A."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The closest cluster to A is B, that is why the first block is a light blue, but it is a pattern due to the variations in compactness."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "If the previous cluster is B, then this cluster must be C as it mirrors the blocks of B."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "As cluster A is the first row, cluster D must be the last row as it mirrors the blocks of A."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # Hierarchical
        # Set of nested clusters organized as a tree
    # Partitional
        # Non-overlapping clusters such that each data object is in exactly one subset

    # Exclusive
        # Assign objects to a single cluster
    # Overlapping/Non-Exclusive
        # An object can simultaneously belong to more than one group (class)
    # Fuzzy
        # Every object belongs to every cluster with a membership weight that is between
        # 0 (does not belong) and 1 (absolutely belongs)

    # Complete
        # Assigns every object to a cluster
    # Partial
        # Does not assign every object to a cluster

    # For each of the described data sets, decide what type of clustering should be used
    # (
    # hierarchical or partitional,
    # exclusive or overlapping or fuzzy,
    # complete or partial (incomplete)
    # )
    # we are using partitional and hierarchical in the more relaxed use of the terms to mean un-nested or nested, respectively.

    # Example: Clustering library books based on their literary genre. The genre/topic can have several subtopics, as well.
    # Answer: hierarchical, overlapping, complete

    # --------- Question A ---------
    # Proteins perform different biological functions that are organized into a hierarchical taxonomy (GO) defined by biologists.
    # Some proteins can be multi-functional as well.
    # You want to group them based on those functions.
    # Some proteins may also be missing functional annotation

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # --------- Question B ---------
    # A nutritionist asks you several questions (e.g., your calorie intake, types of food you eat, your
    # physical activity labels, and so on) to assess your risks for diabetes in three different groups:
    # low, medium, and high.

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # --------- Question C ---------
    # An international grad student can work on campus only at most for 20 hours. You want to
    # assign each student to different job categories (e.g., TA, RA, another on-campus job, jobless).
    # Hint: the sum of these categories should sum up to 20 hours.

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # --------- Question D ---------
    # Grouping of students in a university-based on the organization (department, college, institute, etc.) 
    # to which they belong. A student may belong to multiple organizations. Also, some
    # students dont have declared majors and hence may not belong to any organization

    # type: list
    answers["(d)"] = ['hierarchical', 'overlapping', 'partial']

    # --------- Question E ---------
    # Grouping of all the students in the Computer Science department based on the letter grade
    # they get in the data mining (CSci 5523) class.

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Each cluster is a letter grade and is thus non-overlapping, so it is partitional. A student can only belong to a single letter-grade cluster at a time (not possible to get both an A and a B, if a student has retaken the course then we place them in the most recent grade). Partial as not every student in the computer science department has taken the course."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # Consider the following two sets of points (faces) shown in figures (a) and (b). The darker shading
    # indicates a denser point distribution


    # For each figure, could you use DBSCAN to find clusters corresponding to the patterns represented by the nose, 
    # eyes, and mouth? Explain.

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN would likely discard the low-density regions as noise in figure A, while assuming appropriate EPS and MinPts values would result in figure B being possible to find the patterns represented by the nose, eyes, and mouth."

    # For each figure, could you use K-means to find the patterns represented by the nose, eyes,
    # and mouth? Explain.

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-Means would not find centroids in the nose, eyes, and mouth in figure a) as they are not meaningful areas in the centroid calculation. On the other hand, with K=4, it may be possible to roughly find the patterns in figure b), however these clusters would include the areas of low-density unless they were discarded before hand."

    # For (a), could you figure out a clustering method, which can find the patterns represented by
    # the nose, eyes, and mouth?

    # type: string
    answers["(c)"] = "An adaption of DBSCAN would work where instead of discarding the noise points, the border and core points would instead be discarded. This would leave one with the regions of low-density, representing the nose, eyes, and mouth."

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
