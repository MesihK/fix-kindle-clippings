import re
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-i','--input', type=str, default='clipings.txt')
my_parser.add_argument('-o','--out', type=str, default='out.md', help='Output file')

args = my_parser.parse_args()

clips = list()
page = 0
loc = [0,0]
cont = ''
start = False
with open(args.input,'r',encoding='utf-8') as f:
    for l in f:
        if start and len(l.strip()) > 0:
            cont = l
            start = False
            clips.append([page,loc,cont])

        if l.startswith('-'):
            page = int(re.search(r'page (\d+)',l).groups()[0])
            loc = [int(i) for i in re.search(r'Location (\d+)-(\d+)',l).groups()[0:2]]
            start = True

nclips = list()
last = [0,[0,0],'']
for c in clips:
    if last[0] != c[0]:
        if len(last[2]) > 0:
            nclips.append(last)
        last = c
    else:
        #if same page and loc's intersect, don't take
        if len(set(range(last[1][0],last[1][1])) & set(range(c[1][0], c[1][1]))) > 0:
            last = c
        else:
            nclips.append(last)
            last = c

with open(args.out, 'w', encoding='utf-8') as f:
    f.write('# Clips\n\n')
    for c in nclips:
        f.write('- Page %d loc %d-%d \n\n'%(c[0],c[1][0],c[1][1]))
        f.write('    %s\n'%c[2])
print('Total reduction on clipings: ', len(clips)-len(nclips))

    
    

