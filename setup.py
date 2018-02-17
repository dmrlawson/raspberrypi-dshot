from distutils.core import setup, Extension

module1 = Extension(
    'dshot',
    sources=['dshotmodule.c']
)

setup(
    name='DShot',
    version='0.1',
    description='This package allows the sending of DShot frames to '
                'Raspberry Pi GPIO pins using python code.',
    ext_modules=[module1]
)
