# This is our introductory R code file, where we implemented our first R functions.

add.4 <- function(a, b, c, d) {a + b + c + d}


# Sum range recursive formulation
srr <- function(from, to) {
	if(from == to) { return(from) }
	return(srr(from, to - 1) + to)
}

# Recursively print each element in the vector.
pr <- function(vec) {
	if(length(vec) == 1) {
		message(vec[1])
	}
	else {
		message(vec[1])
		pr(vec[2:length(vec)])
	}
}

# Sum range iterative formulation
sum.range <- function(min.val, max.val) {
	curr.pos <- min.val
	running.total <- 0
	while(curr.pos <= max.val) {
		running.total <- running.total + curr.pos
		curr.pos <- curr.pos + 1
	}	
	running.total
}

quadratic <- function(a, b,d) {
	x<-c((-1*b)+(sqrt (b^2)-(4*a*d))/(2*a),(-1*b)-(sqrt (b^2)-(4*a*d))/(2*a))
	x
}

# Compute the sum of squares for numbers in nums.
# Input: nums is a vector of numbers
# Output: the sum of squares
sum.squares <- function(nums) {
	running.total <- 0
	for(num in nums) { running.total <- running.total + (num * num) }
	return(running.total)
}

nths <- function(vec, n) {
	return(vec[seq(n, length(vec), by = n)])
}

# Aggregate sums of consecutive numbers, n at a time.
n.agg <- function(vec, n) {
	in.i <- 1
	out.i <- 1
	out.vec <- c()
	while(in.i <= length(vec)) {
		last <- min((in.i + n - 1), length(vec))
		curr.sum <- sum(vec[in.i:last])
		out.vec[out.i] <- curr.sum
		in.i <- in.i + n
		out.i <- out.i + 1
	}
	out.vec
}

# Print a solution to hanoi tower.
hanoi <- function(n, strt, finish, other) {
	if(n == 1) {
		cat("Move disk from", strt, "to", finish, "\n")
	}
	else {
		hanoi(n - 1, strt, other, finish)
		cat("Move disk from", strt, "to", finish, "\n")
		#message("special place!")
		hanoi(n - 1, other, finish, strt)
	}
}

# Simple fibonacci  sequence generator.
fib <- function(first, second, n) {
	if(n == 1) { return(first) }
	if(n == 2) { return(second) }
	else { return(fib(first, second, n - 1) + fib(first, second, n - 2)) }
}

# Basic summarizer method.
df.summarize <- function(dframe) {
	for(colmn in colnames(dframe)) {
		vals <- dframe[, colmn]
		if(is.numeric(vals)) {
			cat("Column", colmn, ": mean =", mean(vals, na.rm=TRUE),   "\n")
		}
	}
}




