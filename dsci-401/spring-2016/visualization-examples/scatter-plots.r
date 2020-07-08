# Some scatter plot examples.

data(mtcars)

plot(mtcars$mpg, mtcars$hp)

# Change symbol size
plot(mtcars$mpg, mtcars$hp, cex=2)
  
# Add labels  
plot(mtcars$mpg, mtcars$hp, cex=2, 
   xlab="Miles Per Gallon", 
   ylab="Horse Power",
   main="Engine Power vs. MPG")
   
# Set color
plot(mtcars$mpg, mtcars$hp, col = "blue", cex=2, 
   xlab="Miles Per Gallon", 
   ylab="Horse Power",
   main="Engine Power vs. MPG")

# Change Symbol:
# R Colors and PCH Symbols: http://www.statmethods.net/advgraphs/parameters.html
plot(mtcars$mpg, mtcars$hp, col = 259, pch = 17, cex=2, 
   xlab="Miles Per Gallon", 
   ylab="Horse Power",
   main="Engine Power vs. MPG")

# Scatter Plot - stick shift/automatic different colors and same symbols
plot(mtcars$mpg, mtcars$hp, col = 5 + (mtcars$am > 0), pch=17, cex=2,
   xlab="Miles Per Gallon", 
   ylab="Horse Power",
   main="Engine Power vs. MPG")

# Scatter Plot - stick shift/automatic different colors and symbols
plot(mtcars$mpg, mtcars$hp, col = 5 + (mtcars$am > 0), pch=16 + (mtcars$am > 0), cex=2,
   xlab="Miles Per Gallon", 
   ylab="Horse Power",
   main="Engine Power vs. MPG")

# Add a legend   
legend("topright", lty=1, col=c(5,6), pch=c(16,17), legend=c("Manual", "Automatic"))

