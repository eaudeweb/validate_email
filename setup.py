from setuptools import setup

setup(name='validate_email',
      version='3.0.0.rc1',
      download_url='git@github.com:eaudeweb/validate_email.git',
      py_modules=('validate_email',),
      author='Valentin Dumitru (fork from Syrus Akbary)',
      author_email='valentin.dumitru@eaudeweb.ro',
      description=('validate_email verifies if an email address is valid and '
                   'really exists.'),
      long_description=open('README.rst').read(),
      keywords='email validation verification mx verify',
      url='http://github.com/eaudeweb/validate_email',
      license='LGPL',
      zip_safe=False,
      install_requires=[
          'pydns; python_version<"3.0"',
          'py3dns ; python_version>"3.0"',
      ],
      )
