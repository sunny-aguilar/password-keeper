!# python3
# password keeper
# python script to hold app passwords

PASSWORDS = {'email': '/6ufAbx[#W>]N~',
            'blog': 'O-n\1,?"|~k$Rl',
            'safe': 'Nca6osx5!G&[Dx',
            'locker': 'l!"hH(@"3C!1Ez'}

import sys
if len(sys.argv) < 2:
  print('Usage: python password-keeper.py [account] - copy account password'
  sys.exit()

account = sys.argv[1]     # first command line arg is the account name


