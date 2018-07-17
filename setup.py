from setuptools import setup

long_description = """
This is the long description for sample.
"""

setup(
	name = "sample", # name of your module
	version = "0.0.1", # version of your module
	description = "sample", # a short description
	long_description = long_description, # a long description
	url = "http://example.com", # project homepage URL
	author = "ben", # your name
	author_email = "ben.lin@gogotech.hk", # your email
	  packages=['sample'],  
	keywords = "test", # keywords for your module
	
	#install_requires = [] # if your project has dependencies, list it here
)