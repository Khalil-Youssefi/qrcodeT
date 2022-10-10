from setuptools import setup

setup(
    name='qrcodeT',
    version='v1.0.4',

    url='https://github.com/Khalil-Youssefi/qrcodeT',
    author='Khalil Youssefi',
    author_email='kh4lil@outlook.com',
    python_requires='>=3.6',
    py_modules=['qrcodeT'],
    install_requires=[
    'qrcode[pil]',
    'numpy',
    ],
)
