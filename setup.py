#!/usr/bin/env python
#chmod +x
from setuptools import setup, find_packages


setup(
    name="dungeonsheets",
    version="0.19.0",
    description='Dungeons and Dragons 5e Character Tools',
    author='Mark Wolfman',
    author_email='canismarko@gmail.com',
    url='https://github.com/canismarko/dungeon-sheets',
    license = "GPL-3.0-only",
    packages=["dungeonsheets","dungeonsheets.classes","dungeonsheets.features","dungeonsheets.forms","dungeonsheets.modules","dungeonsheets.monsters","dungeonsheets.spells"],
    install_requires=[
        'fdfgen',
        'npyscreen',
        'jinja2',
        'pdfrw',
        'sphinx',
        'EbookLib',
        'reportlab',
    ],
    entry_points={
        'console_scripts': [
            'makesheets = dungeonsheets.make_sheets:main',
            'create-character = dungeonsheets.create_character:main'
        ]
    },
    include_package_data=True,
    package_data={"":["*.txt"],"dungeonsheets.forms":["*.*"]},
)

#packages=find_packages(where="dungeonsheets", include=["*.py"], exclude=["dungeonsheets.tests*"])
#package_dir={'': 'dungeonsheets'},
#package_data={"":["ToDoNotes.txt"],"forms":["forms/*.txt","forms/*.pdf","forms/*.html","forms/*.tex","forms/*.jpg","forms/*.css"]},