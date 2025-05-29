num <- as.integer(readline("Enter A Number:"))
prime <- TRUE

if(num < 1){
  print("Prime Number is always Positive")
  prime <- FALSE
}else{
  i=2
  while(i<num){
    if (num %% i == 0){
      prime <- FALSE
      break
    }
  i<-i+1
  }
}
print(prime)