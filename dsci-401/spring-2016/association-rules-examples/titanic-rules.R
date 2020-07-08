# Explore assocation rules in Titanic dataset.
# Based on the following tutorial: http://www.rdatamining.com/examples/association-rules
library(arules)

# Basic selection
titanic <- read.csv("titanic-data.csv")
rules <- apriori(titanic)
inspect(rules)

# Show rules with rhs containing "Survived=Yes" or "Survived=No" only
rules <- apriori(titanic,
	# Only rules with minimum of 2 items, support of at least 0.005, and confidence or 0.08
	parameter = list(minlen=2, supp=0.005, conf=0.8), 
	# Select only rules with RHS = "Survived=Yes"
	appearance = list(rhs=c("Survived=Yes", "Survived=No"), default="lhs"),
	control = list(verbose=F))
sorted.rules <- sort(rules, by="lift")
inspect(sorted.rules)

# Find redundant rules
subset.matrix <- is.subset(sorted.rules, sorted.rules)
subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
redundant <- colSums(subset.matrix, na.rm=T) >= 1

# Show which ones are redundant
which(redundant)

# Remove redundant rules
rules.pruned <- sorted.rules[!redundant]
inspect(rules.pruned)

# ------------- VISUALIZATIONS ----------------------
library(arulesViz)

# Get a numeric plot of support & confidence and colored by lift.
plot(rules)

# Get a graph-based plot.
plot(rules, method="graph", interactive=TRUE, shading=NA)

# Get a parallel coordinate plot.
plot(rules, method="paracoord", control=list(reorder=TRUE))