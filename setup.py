from setuptools import setup

setup(
    name="word_exporter",
    version='0.1',
    packages=['word_exporter'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'WordExporter = word_exporter.cli:run'
        ]
    },
)