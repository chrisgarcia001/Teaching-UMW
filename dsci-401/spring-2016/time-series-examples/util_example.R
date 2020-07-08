library(xts)
library(forecast)

ud <- read.csv("utility-data.csv")
peak <- ts(ud$Peak, start=c(2002,5), end=c(2013,8), frequency=12)
plot(peak, col="blue", lwd=2)
off.peak <- ts(ud$Off.Peak, start=c(2002,5), end=c(2013,8), frequency=12)

# Basic decomposition
peak.decomp <- decompose(peak)
plot(peak.decomp)
plot(forecast(peak.decomp))

# More sophisticated decomposition
peak.fit <- stl(peak, s.window="periodic")
plot(peak.fit, col="blue")
plot(forecast(peak.fit, level=c(0.75, 0.9)), col="red", lwd=2)

off.peak.fit <- stl(off.peak, s.window="periodic")
plot(off.peak.fit, col="green")

# Holt Winters
peak.fit <- HoltWinters(peak, beta=TRUE, gamma=TRUE)
plot(peak.fit, col="blue")


