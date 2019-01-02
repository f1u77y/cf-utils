from distutils.core import setup

setup(name='cf-utils',
      version='0.1.0',
      description='CF utilities',
      author='Bogdan Sinitsyn',
      author_email='f1u77y@yandex.ru',
      packages=['cf'],
      scripts=['scripts/cf'],
      install_requires=[
          'requests >=2.20.0',
          'lxml',
          'cssselect',
          'PyYAML',
      ],
      )
