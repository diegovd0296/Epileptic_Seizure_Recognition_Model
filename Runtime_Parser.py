import sys


def process_runtime_arguments():
    """
    
    :return: list with runtime parameters
    """



    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print "Usage: main.py, data-set.csv"
        print "-alg Algorithm that will be used to expand the tree: 1 for ID3, 2 for C4.5"
        print "-mp Amount of mid_points to divide the data-set"
        print "-cv Cross_validation method: 1 for holdout, 2 for bootstrapping"
        print "-nan Amounts of nans to place in test-set"
        print "NOTE: The default values for these arguments are -alg 1 -mp 10 -cv 1 -nan 0"
        print "NOTE The data-set MUST BE the 2nd argument"
        sys.exit(1)

    argvs = []
    for i in range(len(sys.argv)):
        argvs.append(sys.argv[i])

    return argvs

argvs = process_runtime_arguments()

# Get the the values of the runtime parameters
data = argvs[1]
alg = int(argvs[argvs.index("-alg") + 1]) if "-alg" in argvs else 1
mid_points = int(argvs[argvs.index("-mp") + 1]) if "-mp" in argvs else 10
cv_method = int(argvs[argvs.index("-cv") + 1]) if "-cv" in argvs else 1
nan = int(argvs[argvs.index("-nan") + 1]) if "-nan" in argvs else 0