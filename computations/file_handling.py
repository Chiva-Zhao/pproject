from math import log

filename = "tmp.data"
infile = open(filename, 'r')
line = infile.readline()  # Read first line
x = []
y = []
for line in infile:
    word = line.split()
    x.append(float(word[0]))
    y.append(float(word[1]))
infile.close()
print(x, y)


# Transform y coordinates
def f(y):
    return log(y)


for i in range(len(y)):
    y[i] = f(y[i])
# Write out x and y to a two-column file
outfile = open("tmp_out.data", 'w')
outfile.write('# x and y coordinates\n')
for xi, yi in zip(x, y):
    outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()
