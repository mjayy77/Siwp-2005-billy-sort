from setuptools import setup, find_packages

setup(
    name='sorting_algorithms',  
    version='1.0',  
    description='A collection of sorting algorithms',  
    long_description=open('README.md').read(),  
    url='https://github.com/your-username/sorting_algorithms',  
    author='Billy',  
    author_email='billymj77@gmail.com',  
    license='MIT',  
    packages=find_packages(),  
    install_requires=[],  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)