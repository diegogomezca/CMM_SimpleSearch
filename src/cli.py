import argparse

parser = argparse.ArgumentParser(description='CEU Mass Mediator is a tool for searching metabolites in different databases')
parser.add_argument('--version', action='version', version='1.0')
args = vars(parser.parse_args())
print(args)