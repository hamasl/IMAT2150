import math

if __name__ == "__main__":
    short_leg = 1.2222222
    long_leg = 3344556600
    diff_hyp_long_leg = (short_leg**2)/(math.sqrt(short_leg**2+long_leg**2)+long_leg)
    #TODO exercises ask for rounding to 4 digits, but this is not done
    print(f"Hypotenuse is {diff_hyp_long_leg} longer than the longest leg of {long_leg}")