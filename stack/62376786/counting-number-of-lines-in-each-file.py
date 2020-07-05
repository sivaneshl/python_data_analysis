import glob
with open('count.txt' , 'w') as out:
    filelist = glob.glob('*_file')
    for filename in filelist:
        with open(filename, 'r') as fn:
            count = sum(1 for line in fn)
            out.write('{c} {f}\n'.format(c = count, f = filename))
