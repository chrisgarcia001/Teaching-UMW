# This app allows interactive exploration of Swiss socioeconomic
# relationships.

library(shiny)
data(swiss)


shinyServer(function(input, output) {

  # OUTPUT 1: Build clustering plot
  output$distPlot <- renderPlot({
    #fit <- kmeans(swiss, 3) # Begin with 3
    fit <- kmeans(swiss, input$k)
    fitdata <- cbind(swiss, classif=fit$cluster)
    plot(fitdata[,input$selectedAttributes], col=1+fitdata$classif, pch=16)
  })
  
  # OUTPUT 2: Predict Education by slider values
  output$predEducation <- renderText({
    mod <- lm(Education ~ ., data=swiss)
    df <- data.frame(Fertility=input$Fertility, Agriculture=input$Agriculture, Examination=input$Examination,
                     Catholic=input$Catholic, Infant.Mortality=input$Infant.Mortality)
    pred.val <- predict(mod, df, interval="predict")[1]
    paste("Predicted Post-Secondary Education %:", pred.val)
  })

})
