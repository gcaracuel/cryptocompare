from setuptools import setup

with open('README.rst', encoding="utf-8") as f:
    readme = f.read()

setup(
        name='python-cryptocompare',
        version='0.1',
        description='Wrapper for CryptoCompare.com [FULL]',
        long_description=readme,
        url='https://github.com/gcaracuel/cryptocompare',
        author='gcaracuel',
        author_email='gcaracuel@g_m_a_i_l.com',
        keywords='crypto cryptocurrency wrapper cryptocompare',
        license='MIT',
        python_requires='>=3',
        packages=['cryptocompare'],
        classifiers=['Programming Language :: Python :: 3'],
        install_requires=['requests']
        )
