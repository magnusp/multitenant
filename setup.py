# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='multitenant',
    version='0.1.0',
    license='MIT',
    author='Magnus Persson',
    author_email='magnus.e.persson@gmail.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=["Flask",
                      "Flask-SQLAlchemy",
                      "alembic",
                      "psycopg2",
                      "jinja2"
                      ],
    include_package_data=True,
    classifiers=[
        "Private :: Do Not Upload"
    ],
)
