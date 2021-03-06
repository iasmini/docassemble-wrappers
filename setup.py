from setuptools import setup

setup(
    name='docassemble_wrappers',
    version='0.0.2',
    packages=['docassemble_wrappers'],
    url='https://github.com/silexsistemas/docassemble-wrappers',
    license='MIT',
    author='Roberto Vasconcelos Novaes',
    author_email='roberto.novaes@silexsistemas.com.br',
    description='Wrappers to external functionalities and Docassemble API',
    install_requires=[
        'validator-collection-br',
    ],
)
