# python/python-3.6.7

import os
import logging
import shutil
import datetime

if __name__ == '__main__':
        from sys import argv

        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('path',
                            help='A path to a folder in which the sweeps analysis will be written.',
                            type=lambda path: path if os.path.exists(path) else parser.error(f'{path} does not exist!'))
        parser.add_argument('jobID', type=str,
                            help='The size of a window to which a score will be computed')
                            
        args = parser.parse_args()
        
        results_dir = os.path.join('/bioseq/data/results/CLUMPAK', args.jobID)
        logFile = os.path.join( results_dir, 'output.log')
        end_line = f'Job {args.jobID} has finished running.'
        status = 'FAIL'
        try:
            with open(logFile, "r") as f: 
                for line in f: 
                    if end_line in line: 
                        status = 'PASS'
            f.close()
        except: 
            pass
        
        results_url = f'http://clumpak.tau.ac.il/results.html?jobId={args.jobID}'
        date = datetime.datetime.today().strftime('%d%m%Y')
        with open(os.path.join(args.path, f'clumpak_{date}.txt'), "w") as f:
            f.write(f'{status},{results_url}')
        f.close()
        
        

        
       

