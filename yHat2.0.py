class yHat:

    def calc_a(self):
        r = float(input("Enter the correlation coefficient of the problem: "))
        s_a = float(input("Enter the standard deviation for the 'Y' variable data set: "))
        s_x = float(input("Enter the standard deviation for the 'X' variable data set: "))
        b = r * (s_a/s_x)
        print("")
        print("**The 'b' value for the equation is: ", (float(round(b, 4))))
        print("")
        y_bar = float(input("Enter the 'Y' avg: "))
        x_bar = float(input("enter the 'X' avg: "))
        a = y_bar - (b * x_bar)
        print("The 'Y' avg is: ", (float(y_bar)))
        print("The 'X' avg is: ", (float(x_bar)))
        print("")
        print("**The 'a' value for the equation is: ", (float(round(a, 4))))
        print("")
        print("yHat formula: yHat = a + b(x)")
        print("")
        return 'done'


a = yHat()
print(a.calc_a())
