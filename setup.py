from setuptools import setup

from qrcodeT import __version__

setup(
    name='qrcodeT',
    version=__version__,

    url='https://github.com/Khalil-Youssefi/qrcodeT',
    author='Khalil Youssefi',
    author_email='kh4lil@outlook.com',
    python_requires='>=3.6',
    py_modules=['qrcodeT'],
    install_requires=[
    'qrcode[pil]',
    ],
)
