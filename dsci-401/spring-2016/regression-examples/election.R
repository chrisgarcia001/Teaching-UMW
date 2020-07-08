# Use Year 2000 election data to predict who would vote for Bush

ed <- read.csv("election-2000.csv")
ed <- ed[2:length(ed)] # Remove State column
em <- lm(Bush. ~ ., data=ed)
summary(em)