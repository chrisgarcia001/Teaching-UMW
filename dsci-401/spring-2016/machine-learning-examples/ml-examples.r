# Kappa statistic notes: http://standardwisdom.com/softwarejournal/2011/12/confusion-matrix-another-single-value-metric-kappa-statistic/

library(caret)

# Load the iris dataset
data(iris)

# ------ PART I: Basic machine learning illustration with random forest.
# SIDE NOTE -  Info on ML algorithms available with caret here: http://topepo.github.io/caret/bytag.html

# Create an 80%/20% train/test split of the dataset
split=0.80
trainIndex <- createDataPartition(iris$Species, p=split, list=FALSE)
train.data <- iris[ trainIndex,]
test.data <- iris[-trainIndex,]

# Train a Random Forest model
modelFit <- train(Species ~.,data=train.data, method="rf")

# Predict for Test Set
predictions <- predict(modelFit, newdata=test.data)

# Summarize results
confusionMatrix(predictions, test.data$Species)

# ------ PART II: Using k-fold crossvalidation
# Define training control
train_control <- trainControl(method="cv", number=10)

# Train the model with 10-fold CV
kf.model <- train(Species~., data=iris, trControl=train_control, method="rf")

# Summarize results
print(kf.model)


# ------ PART III: Leave-one-out crossvalidation
# Define training control
train_control <- trainControl(method="LOOCV")

# Train the model with 10-fold CV
loo.model <- train(Species~., data=iris, trControl=train_control, method="rf")

# Summarize results
print(loo.model)

