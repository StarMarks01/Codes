num <- as.numeric(readline("Enter a number:"))
if(is.na(num)){
  print("Invalid Input! Try again")
}else{
  if(num %% 2 == 0){
    print("This is an Even Number")
  }else{
    print("This is an Odd Number")
  }
}
i = 1
while(i<=100){
  if(i%%2==0){
    print(paste("Even Number:",i))
  }
  else{
    print(paste("Odd Number",i))
  }
  i=i+1
}

