from distutils.core import setup

setup(name='cf-utils',
      version='0.1.0',
      description='CF utilities',
      author='Bogdan Sinitsyn',
      author_email='bogdan.sinitsyn@gmail.com',
      packages=['cf'],
      scripts=['scripts/cf'],
      install_requires=[
          'requests ==2.18.1',
          'lxml ==3.8.0',
          'cssselect ==1.0.1',
          'PyYAML ==3.12',
      ],
      )
