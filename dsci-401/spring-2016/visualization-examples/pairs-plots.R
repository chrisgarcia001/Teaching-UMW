data(mtcars)
require(graphics)
subs <- mtcars[c(1,3,4,5,6,7,9)] # Subset of most clearly related to MPG

pairs(subs)
pairs(subs, panel = panel.smooth) # Add in a trend line

# Add in a title separate based on whether car is automatic or manual.
pairs(subs, panel = panel.smooth, 
   main = "MT Car Data (Subset) Divided by Manual and Automatic", 
   col = 5 + (mtcars$am > 0))
