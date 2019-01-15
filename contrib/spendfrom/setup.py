from distutils.core import setup
setup(name='BKSspendfrom',
      version='1.0',
      description='Command-line utility for BKS "coin control"',
      author='Gavin Andresen',
      author_email='gavin@BKSfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
