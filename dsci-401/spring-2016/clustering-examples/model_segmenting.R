library(mclust)
library(cluster)

# Load data
dataset <- read.csv("purchases.csv", row.names=1)

# Optional: Scale the data before computing distances between rows - all columns carry equal weight.
ind <- 1:ncol(dataset)
dataset[ind] <- lapply(dataset[ind], scale)

# Build latent cluster model and show results
fit <- Mclust(dataset)
print(fit$BIC) # Show the fit summary
classif <- fit$classification # The segment classification vector - class of each person
fitdata <- cbind(dataset, classif=classif) # Add the classes to the data as a new column

# Display cluster plot based on two latent components and show cross-var plots
plot(fitdata, col=1+fitdata$classif)
dev.new()
clusplot(dataset, fitdata$classif, color=TRUE, shade=TRUE, labels=2, lines=0)
