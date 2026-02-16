from setuptools import setup

setup(
    name='repochecker',
    description='CLI to check status of git repositories',
    author='Oli',
    author_email='oli@olillin.com',
    license='MIT',
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'repochecker=repochecker:main',
        ]
    },
)
