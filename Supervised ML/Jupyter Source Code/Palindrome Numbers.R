pal <- 101
n <- pal
i <- 1
sum = 0
while(n>0){
  rem <- n%%10
  sum <- sum + rem^3
  n <- n%/%10
}
print(sum)
