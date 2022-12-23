import argparse
import math



# parser = argparse.ArgumentParser()
# parser.add_argument('-r','--repeat',type=int,help='number of repeat')
# argx = parser.parse_args()


# def justTry(*args):

#     x = args

#     print(args)



# justTry(argx.repeat)


parser = argparse.ArgumentParser(description='calculate')
parser.add_argument('-r','--radius',type=int,help='radius of cylinder')
parser.add_argument('-H','--height',type=int,help='height of cylinder')
args = parser.parse_args()

def cylinder_vol(radius, height):

    vol = (math.pi) * (radius ** 2) * (height)
    return vol


if __name__ == '__main__':

    print(cylinder_vol(args.radius, args.height))
