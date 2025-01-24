from setuptools import setup, find_packages

setup(
    name='calculator',  
    version='0.1',  
    packages=find_packages(),  
    install_requires=['sys',
        'gui',
        'PyQt6.QtWidgets',
        'math',
        'matplotlib.pyplot',
        'numpy',
        'setuptools',
        'unittest'
        
    ],
    entry_points={
        'console_scripts': [
            'your_command=main:main_function', 
        ],
    },
    author='Polinka',
    license='MIT',
    url='https://github.com/asfqx/calculator/tree/main',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
    ],
    python_requires='>=3.6',  
)
