from setuptools import setup

setup(
    name='extendedBuiltins',
    version='0.1',
    description='todo: add description',
    url='https://github.com/extendedBuiltins/extendedBuiltins',
    author='Romain J.',
    author_email='romain.ordi@gmail.com',
    license='MIT',
    packages=[
        'extendedBuiltins',
        'extendedBuiltins.core',
        'extendedBuiltins.tests'
    ],
    python_requires='>=3.6',
    zip_safe=False,
    install_requires=[
        "pytest",
    ],
    scripts=['runtests'],
)

