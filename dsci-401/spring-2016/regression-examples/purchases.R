# Illustrates a logistic regression model to predict liklihood of 
# purchase on a website.

# Load the data and build the logistic regression model from all predictors.
purchases <- read.csv("website-purchases.csv")
logit.mod <-  glm(Buy ~ ., data=purchases, family = "binomial")
summary(logit.mod)

# Use bidirectional stepwise variable selection to find the best model. 
library(MASS)
best.fit <- stepAIC(logit.mod, direction="both")

# Evaluate the fits of both models.
with(logit.mod, pchisq(null.deviance - deviance, df.null - df.residual, lower.tail = FALSE))
with(best.fit, pchisq(null.deviance - deviance, df.null - df.residual, lower.tail = FALSE))

# Read in a set of new data not used to build the model, make predictions using best model, and see how they compare. 
new.purch <- read.csv("new-web-purchases.csv")
probs <- predict(best.fit, newdata=new.purch, type = "response") # Get probabilities
predictions <- round(probs)  # Get a 0 or 1 class label

results <- data.frame(actual.buy=new.purch$Buy, predicted.buy=predictions, probability.buy=probs) # Make a dataframe with comparison results
print(results) 

