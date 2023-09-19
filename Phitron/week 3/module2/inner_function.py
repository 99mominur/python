def do_something():
    print("inside the do_something")

    def inside_something():
        print("I am from inside_something")
    return inside_something


work = do_something()

work()
