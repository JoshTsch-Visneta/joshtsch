from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='joshtsch',
    version='0.1',
    description="",
    long_description="",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business',
    ],
    url="",
    author='josh_tsch',
    author_email='joshtscheschlogassero@gmail.com',
    packages=['joshtsch'],
    install_requires=[
        'pyyaml',
        'logging',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],)