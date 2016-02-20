import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mosaico',
    version='0.1',
    packages=find_packages('.'),
    include_package_data=True,
    license='BSD License',  # example license
    description='A django app that contains the mosaico frontend and implements the mosaico backend.',
    long_description=README,
    url='http://www.github.com/tubaman/django-mosaico/',
    author='Ryan Nowakowski',
    author_email='tubaman@fattuba.com',
    install_requires = ['django>=1.9', 'django-jsonfield>=0.9.16', 'django-jsonify'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
