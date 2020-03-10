import os
import tensorflow as tf 
import argparse
import subprocess
from argparse import RawTextHelpFormatter
import pyfiglet
import numpy
from model import build_model

allowed = '-ABCDEFGHIKLMNPQRSTVWY'
size_allowed = [30,50,70,90,95]
ascii_banner = pyfiglet.figlet_format("Welcome to\n Secondary Structure Proteinn prediction!")
desc_usg = ascii_banner + '''usage: python3 SecStrPred.py build <train_size>
Prerequisite: Download Proteinnet data and store the data in the data folder included.'''

parser = argparse.ArgumentParser(description=desc_usg, usage=argparse.SUPPRESS, formatter_class=RawTextHelpFormatter)
subparser = parser.add_subparsers(help="""Available commands are:
build <train_size> - Builds a trained model trained on either 30, 50, 70, 90 or 95 CASP training examples
Using all data for training will make an overlap in training.
run /path/to/local/sequence/ - Enter local sequence to predict secondary structure.
""", dest='command')
# run_parser = subparser.add_parser('run')
# run_parser.add_argument('sequence', 'The full path to sequence file.')
train_parser = subparser.add_parser('build')
train_parser.add_argument('train_size', help='CASP training data size, sizes are 30, 50, 70, 90 or 95, default is 95', type=int, default=95)
train_parser.add_argument('casp_ver', help='')
def main(args):
    if np.isin(size_allowed, train_size):
        print('Error! Invalid data size')
        return
    print('No model yet')
    # model = build_model(train_size)
    # dist_pred, dist_loss = domain(args.domain, network, args.stride)
    # p = dist_pred.detach().numpy()
    # save_path = pconf.basedir+args.domain +"/"
    # save(p, save_path + args.domain +'_'+'_'+str(args.stride)+'_predictions.pkl')
    # print("contact predictions saved in %s" % save_path)
    # print('\nAnalyze prediction results: https://github.com/dellacortelab/prospr\n')
    
    return

def build(args):
    if np.isin(size_allowed, train_size):
        print('Error! Invalid data size')
        
        return

    return

if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == 'run':
        main(args)
    elif  args.command == 'build':
        build(args)
