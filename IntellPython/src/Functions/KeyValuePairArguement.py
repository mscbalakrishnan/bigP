def varFunc(name, roll, **option):
        print("Name: "+name)
        print("Roll: "+str(roll))
        if "age" in option :
                print("Age: "+ str(option.get("age")))
        if "gender" in option:
                print("Gender: "+ str(option.get("gender")))

print("First Person")
varFunc("Alice", 234, age=18, gender="female")

print("\nSecond Person")
#See, the order of argument age and gender is different now
varFunc("Bob", 204, gender="male", age=21)

print("\nThird Person")
#We will not pass age as and argument
varFunc("Trudy", 204, gender="male")