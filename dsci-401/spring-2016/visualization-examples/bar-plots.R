# These examples are essentially enhanced versions of those from "R in a Nutshell", 2E 
# By Joseph Adler.

doctorates <- read.csv("doctorates.csv")

# Barplots require a matrix as input, not a dataframe.
dm <- as.matrix(doctorates[2:7])
rownames(dm) <- doctorates[, 1] # Set the year to be row names/labels
dm

# Print first year - 2001
barplot(dm[1,])

# Change the color
barplot(dm[1,], col="blue")

# Build year-based comparison plot
barplot(dm, beside=TRUE, horiz=TRUE, legend=TRUE, cex.names=0.75)

# Add title and use different colors each year:
barplot(dm, beside=TRUE, horiz=TRUE, legend=TRUE, cex.names=0.75,
		main="Doctorates in US by Year and Discipline",
		col=c("blue","red","green","yellow","orange","purple"))
		
# Build a stacked plot. To do this we must transpose data (i.e. flip rows and columns).
# We transpose using the "t" function.
barplot(t(dm), legend=TRUE, ylim=c(0,70000))

# Add title and use different colors each year:
barplot(t(dm), legend=TRUE, ylim=c(0,70000),
		main="Doctorates in US by Year and Discipline",
		col=c("blue","red","green","yellow","orange","purple"))

		
