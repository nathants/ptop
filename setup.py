import setuptools

setuptools.setup(
    version="0.0.1",
    license='mit',
    name='ptop',
    author='nathan todd-stone',
    author_email='me@nathants.com',
    url='http://github.com/nathants/ptop',
    scripts=['ptop'],
    python_requires='>=3.7',
    install_requires=['psutil',
                      'argh',
                      'blessed'],
    description='a minimal htop alternative',
)
