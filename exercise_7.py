x = "Hello!" 
y = 20
z = 1.23

print(type(x))
print(type(y))
print(type(z))

y += z
print(y)
print(type(y)) # 2.y should now be a float as well

y += int(z)
print(y)
print(type(y)) #3. it's adding on to y every time so it is still a float, if i removed the previous line it would be an integer

str(z)
print(str(z))
# 4. I don't think it changes the type of z it just prints it as a string?

# 5. No, we can't add a string to an integer or float