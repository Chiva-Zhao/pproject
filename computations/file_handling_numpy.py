import numpy

infile = "tmp.data"
outfile = "tmp_out.data"
data = numpy.loadtxt(infile, comments='#')
x = data[:0]
y = data[:1]
data[:1] = numpy.log(y)

ofile = open(outfile, 'w')
ofile.write('# x and y coordinates\n')
numpy.savetxt(outfile, data, '%10.5f')
