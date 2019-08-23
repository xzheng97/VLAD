import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
        help = "Path of a query image")
#ap.add_argument("-r", "--retrieve", required = True,
#	help = "number of images to retrieve")
#ap.add_argument("-d", "--descriptor", required = True,
#	help = "descriptors: SURF, SIFT or ORB")
#ap.add_argument("-dV", "--visualDictionary", required = True,
#	help = "Path to the visual dictionary")
#ap.add_argument("-i", "--index", required = True,
#	help = "Path of the Ball tree")
args = vars(ap.parse_args())


path = args["query"]
#k=int(args["retrieve"])
#descriptorName=args["descriptor"]
#pathVD = args["visualDictionary"]
#treeIndex=args["index"]

print("hello world " + path)


