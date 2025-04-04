m <- 5000
while(TRUE){
  print("1. Deposit")
  print("2. Withdraw")
  print("3. EXIT")
  print(paste("Current Balance",m))
  choice <- as.numeric(readline("Enter Your Choice:"))
  if(choice == is.na(choice)){
    print("Invalid Input! Please enter a valid choice:")
  }else if(choice == 1){
    dep <- as.numeric(readline("Enter The Amount to deposit:"))
    m <- m + dep
    print(m)
    if(is.na(dep)){
      print("Invalid Input! Please enter the amount to deposit")
    }
  }else if(choice == 2){
    wit <- as.numeric(readline("Enter The Amount to withdraw:"))
    m <- m - wit
    print(m)
    if(is.na(wit)){
      print("Invalid Input! Please enter the amount to deposit!")
    }
  }else if(choice == 3){
    break
  }else{
    print("Invalid Input")
  }
}
  
  