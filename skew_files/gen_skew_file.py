#!/usr/bin/python

import argparse

def parse_skew(node_map,skew_map,output_file):
    # expects root directory to have structure as follows: {root_dir}/{algorithm}/{dataset}/LOG_{partition}.out"
    with open(node_map, 'r') as nm_f:
        with open(skew_map, 'r') as sm_f:
            with open(output_file, 'w') as of_f:
                sm = {}
                for line in sm_f:
                    l = line.strip().split(" ")
                    if l[0][0] != "#" and l[0] != "":
                        sm[l[0]] = l[1]
                #print sm   
                for line in nm_f:
                    l = line.strip().split(" ")
                    if l[0][0] != "#" and l[0] != "":
                        #print l
                        of_f.write(l[0] + " " + sm[l[1]] + "\n")                   
	        of_f.close()
	    sm_f.close()
        nm_f.close()
                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parses PowerLyra outputs")
    parser.add_argument("node_map", help="Mapping of hostnames to EC2 instance types")
    parser.add_argument("skew_map", help="Mapping of EC2 instance types to skew factors")
    parser.add_argument("output_file", help="Name of the output skew file to create")
    args = parser.parse_args()
    parse_skew(args.node_map, args.skew_map, args.output_file)
