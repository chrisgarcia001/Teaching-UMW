library(cluster)

# Load data
dataset <- read.csv("purchases.csv", row.names=1)

# Optional: Scale the data before computing distances between rows - all columns carry equal weight.
ind <- 1:ncol(dataset)
dataset[ind] <- lapply(dataset[ind], scale)

# Build the hierarchical cluster based on Euclidean row distances computed from all columns.
clusters <- hclust(dist(dataset)) 
clusters <- hclust(dist(dataset), method='average') # This will use a different linkage method
plot(clusters)
plot(clusters, hang=-1) # The hang option puts all row labels at the same vertical level. Looks a little nicer.

# Cut the cluster into 3 groups, based on looking at the dendrogram.
cluster.cut <- cutree(clusters, 3)
print(head(cluster.cut))  # show the cuts
table(cluster.cut)        # show the number of people in each cluster

# Add the cluster of membership to each person
fitdata <- cbind(dataset, classif=cluster.cut) 

# Display cluster plot based on two latent components and show cross-var plots
plot(fitdata, col=1+fitdata$classif)
dev.new()
clusplot(dataset, fitdata$classif, color=TRUE, shade=TRUE, labels=2, lines=0)
