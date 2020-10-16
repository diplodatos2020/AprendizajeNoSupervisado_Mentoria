# -*- coding: utf-8 -*-

"""
Set-up
-----------------
"""

from distutils.core import setup


setup(
    name='mentoria-ans',
    version='1.0',
    description='Aprendizaje no supervisado',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'jupyterlab',
        'scikit-learn',
        'tslearn',
        'scipy'
    ]
)
