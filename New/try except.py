try:
    print(a)
    print(10 / 5)
except Exception as e:
    print("error code",e)
else:
    print("There is no error")
finally:
    print("This will always execute")
