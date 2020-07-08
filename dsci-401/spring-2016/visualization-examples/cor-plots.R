# Super-easy to use correlation plotting package
# Examples from http://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html

library(corrplot)
M <- cor(mtcars) # Builds a correlation matrix
corrplot(M, method = "color") # Pure color showing correlations
corrplot(M, method = "number") # Color and correlation coeff. depicting
corrplot(M, method = "ellipse") # Color, direction, and thinness of ellipse depicts correlation
corrplot(M, method="color", type = "lower") # Only bottom half by color
corrplot.mixed(M, lower="number", upper="ellipse")