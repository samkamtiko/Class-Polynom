import unittest
import platform
from setuptools import setup, find_packages, Command
from setuptools.command.test import test

if platform.system() == 'Linux':
    from colour_runner.result import ColourTextTestResult


class DoTest(test):
    test_args = []
    test_suite = True

    @staticmethod
    def __generate_test_suite():
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests', pattern='*_test_case.py')
        return test_suite

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run_tests(self):
        test_suite = self.__generate_test_suite()
        if platform.system() == 'Linux':
            test_runner = unittest.runner.TextTestRunner(verbosity=2, resultclass=ColourTextTestResult)
        else:
            test_runner = unittest.runner.TextTestRunner(verbosity=2)
        test_runner.run(test_suite)


class ComputeCoverage(Command):
    description = "Generate a test coverage report."
    user_options = []

    def initialize_options(self): pass

    def finalize_options(self): pass

    @staticmethod
    def run():
        import subprocess
        subprocess.call(['coverage', 'run', '--source=polynome', 'setup.py', 'test'])
        subprocess.call(['coverage', 'report', '-m'])
        subprocess.call(['coverage', 'html'])


setup(
    name='polynome',
    version='0.1',
    description='Training project',
    author='Sam Kamtiko',
    author_email='samkamtiko2012@gmail.com',
    packages=find_packages(exclude=['tests']),
    cmdclass={'coverage': ComputeCoverage,
              'test': DoTest},
    setup_requires=[ 'coverage' ]
)
