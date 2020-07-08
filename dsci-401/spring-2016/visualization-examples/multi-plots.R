pd <- read.csv("product-sales.csv")

# Example 1: Plot each line in a different graph.
par(mfrow = c(3, 1))  # Use 3 rows and 1 column.
plot(pd$week, pd$product.1, type="b", col="green", lwd=2, pch=16, cex=2)
plot(pd$week, pd$product.2, type="b", col="blue", lwd=2, pch=17, cex=2)
plot(pd$week, pd$product.3, type="b", col="red", lwd=2, pch=18, cex=2)

# Example 2: Save to file
png(file = "line-graphs.png") # STEP 1: Tell to start writing to file
# STEP 2: Tell what to write (below): 
par(mfrow = c(3, 1))  # Use 3 rows and 1 column.
plot(pd$week, pd$product.1, type="b", col="green", lwd=2, pch=16, cex=2)
plot(pd$week, pd$product.2, type="b", col="blue", lwd=2, pch=17, cex=2)
plot(pd$week, pd$product.3, type="b", col="red", lwd=2, pch=18, cex=2)
dev.off() # STEP 3: Tell to stop writing and create file


