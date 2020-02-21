import snowlipse 
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

build_requires = ['Pillow', 'matplotlib', 'numpy']

tests_require = []

packages = find_packages()


metadata = dict(name='snowlipse',
                maintainer='Nick Kypreos',
                maintainer_email='',
                description='',
                license='',
                url='',
                version=snowlipse.__version__,
                download_url='',
                long_description='',
                packages=packages,
                entry_points={
                          'console_scripts': [
                              'snowlipse-toy=snowlipse.snowlipse:toy'
                          ]
                },
                install_requires=build_requires,
                build_requires=build_requires,
                tests_require=tests_require)

setup(**metadata)
