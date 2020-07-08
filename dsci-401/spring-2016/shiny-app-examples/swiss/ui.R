# This app allows interactive exploration of Swiss socioeconomic
# relationships.

library(shiny)
data(swiss)

shinyUI(fluidPage(

  # Application title
  titlePanel("Swiss Socioeconomic Exploration (circa 1888)"),

  # Sidebar with a set of appropriate inputs for cluster plot and regression prediction
  sidebarLayout(
    sidebarPanel(
      checkboxGroupInput("selectedAttributes", label = h4("Cluster Attributes Shown"), 
                         choices = colnames(swiss),
                         selected = c("Fertility", "Agriculture", "Catholic")),
      sliderInput("k", "Number of cluster means (k):", min = 2, max = 5, value = 3),
      h4("Predict % Pose-Secondary Education:"),
      sliderInput("Fertility", "Fertility:", min = min(swiss$Fertility), 
                  max = max(swiss$Fertility), value = mean(swiss$Fertility)),
      sliderInput("Agriculture", "Agriculture:", min = min(swiss$Agriculture), 
                  max = max(swiss$Agriculture), value = mean(swiss$Agriculture)),
      sliderInput("Examination", "Examination:", min = min(swiss$Examination), 
                  max = max(swiss$Examination), value = mean(swiss$Examination)),
      sliderInput("Catholic", "Catholic:", min = min(swiss$Catholic), 
                  max = max(swiss$Catholic), value = mean(swiss$Catholic)),
      sliderInput("Infant.Mortality", "Infant Mortality:", min = min(swiss$Infant.Mortality), 
                  max = max(swiss$Infant.Mortality), value = mean(swiss$Infant.Mortality))
    ),
    

    # Show the generated results
    mainPanel(
      h4("Cluster Plot"),
      plotOutput("distPlot"), 
      h4(textOutput("predEducation"))
    )
  )
))
