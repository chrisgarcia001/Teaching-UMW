# Example 1: Explore regression with car data
#            Basic regression usage.

data(mtcars)

# Model 1: MPG = B0 + B1*HP + epsilon
m1 <- lm(mpg ~ hp, data=mtcars)
summary(m1)

# Plot HP to MPG relationship
plot(mtcars$hp, mtcars$mpg, col="blue", pch=16, cex=1.5)
abline(lm(mpg ~ hp, data=mtcars), col="red", lwd=2) # Add a best-fit line

# Model 2: MPG = B0 + B1*HP + B2*WT + B3*DISP + epsilon
m2 <- lm(mpg ~ hp + wt + disp, data=mtcars)
summary(m2)

# Model 3: MPG = B0 + B1*HP + B2*WT + B3*CYL + epsilon
m3 <- lm(mpg ~ hp + wt + cyl, data=mtcars)
summary(m3)

# Model 4: MPG as function of all other variables
m4 <- lm(mpg ~ ., data=mtcars)
summary(m4)

# Use stepwise variable selection on m4 (all variables) to get best set of predictors
library(MASS)
best.fit <- step <- stepAIC(m4, direction="both")
summary(best.fit)

# Predict values for new observations
new.cars <- read.csv("cars.csv")
predict(best.fit, new.cars, interval="predict", level=0.95)

# Test the VIF's for two models
library(car)
vif(m4)
vif(best.fit)


