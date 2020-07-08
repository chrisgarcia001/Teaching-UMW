# Line plot examples

pd <- read.csv("product-sales.csv")

# Build a basic line graph.
plot(pd$week, pd$product.1, type="l")

# Make a thicker line (lwd)
# Options: # R Colors and PCH Symbols: http://www.statmethods.net/advgraphs/parameters.html
plot(pd$week, pd$product.1, type="l", lwd=2)

# Make line dashed (lty)
plot(pd$week, pd$product.1, type="l", lwd=2, lty=2)

# Multiple Lines with title
plot(pd$week, pd$product.1, type="l", col="green", lwd=2,
     main="Comparison of Product Sales",
	 xlab="Week", ylab="Sales")
lines(pd$product.2, type="l", col="blue", lwd=2, lty=2)
lines(pd$product.3, type="l", col="red", lwd=2, lty=6)

# Lines with symbol markers (type = "b", pch for symbol, cex for symbol size)
plot(pd$week, pd$product.1, type="b", col="green", lwd=2, pch=16, cex=2,
     main="Comparison of Product Sales",
	 xlab="Week", ylab="Sales", ylim=c(0,40))
lines(pd$product.2, type="b", col="blue", lwd=2, pch=17, cex=2)
lines(pd$product.3, type="b", col="red", lwd=2, pch=18, cex=2)

# Add Legend
legend("topright", lty=1, col=c("green","blue","red"), pch=c(16,17,18), 
      legend=c("Product 1", "Product 2", "Product 3"))
	  