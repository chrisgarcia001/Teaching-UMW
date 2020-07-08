 rd <- read.csv("batting-angles-distances.csv")
 rd
 
 # Build quadratic regression points for each angle, based on formula: Distance ~ Angle*Angle + Angle
 # I(rd$Angle^2) creates a quadratic variable (Angle x Angle)
 # Can also do poly(rd
 yvals <- predict(lm(rd$Distance ~ I(rd$Angle^2) + rd$Angle), newdata=data.frame(Angle=rd$Angle))
 
 #Another way using poly to create a polynomial for Angle of maximum degree 2.
 yvals <- predict(lm(rd$Distance ~ poly(rd$Angle, 2)), newdata=data.frame(Angle=rd$Angle))
 
 plot(rd$Angle, rd$Distance, col="blue", pch=19)
 lines(rd$Angle, yvals, col="red")
 
 #------------ Manual way
 rd$AngleSq <- rd$Angle^2
 yvals <- predict(lm(rd$Distance ~ rd$AngleSq + rd$Angle), newdata=data.frame(Angle=rd$Angle))
 plot(rd$Angle, rd$Distance, col="blue", pch=19)
 lines(rd$Angle, yvals, col="red") 
 
 
 
 