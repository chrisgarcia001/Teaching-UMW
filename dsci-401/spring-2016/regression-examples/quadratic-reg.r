# Illustrate how to deal with cases where the data is clearly not linear
rd <- read.csv('batting-angles-distances.csv')
head(rd)

# Put data in order by Angle to ensure correct trend line drawing
rd <- rd[order(rd$Angle), ]
head(rd) # Notice it is in order now

# Look at the data
plot(rd$Angle, rd$Distance, col="blue", pch=19)

# Build a linear fit to see how it does
linear.mod <- lm(Distance ~ Angle, data=rd)
summary(linear.mod)
linear.preds <- predict(linear.mod, newdata=rd)
lines(rd$Angle, linear.preds, col="black", lwd=2)

# Add an Angle^2 column
rd$AngleSq <- rd$Angle^2
head(rd)

# Build our quadratic model
quad.mod <- lm(Distance ~ AngleSq + Angle, data=rd)

# Look at the summary
summary(quad.mod)

# Make predictions based on quadratic fit model
quad.preds <- predict(quad.mod, newdata=rd)

# Plot the regression line
lines(rd$Angle, quad.preds, col="red", lwd=2)

