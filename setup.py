from setuptools import setup

setup(
    name='jupyter_slack',
    version='2.1.4',
    packages=['jupyter_slack'],
    url='https://github.com/keitakurita/jupyter-slack-notify',
    license='MIT',
    author='keitakurita',
    author_email='keita.kurita@gmail.com',
    description='A magic command for notifying the status of code completion in jupyter notebooks via slack',
    install_requires=['requests', 'ipython', 'jupyter'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
