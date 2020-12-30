import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
    
    
setuptools.setup(name='pythonFTP',
    version='0.0.1',
    description='FTP file transfer and management by Python',
    url='https://github.com/AsajuHuishi/FTP_file_transfer_management',
    author='AsajuHuishi',
    author_email='zengxinyang@tju.edu.cn',
    license='MIT',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False)
      
# import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
    # long_description = fh.read()

# setuptools.setup(
    # name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    # version="0.0.1",
    # author="Example Author",
    # author_email="author@example.com",
    # description="A small example package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # packages=setuptools.find_packages(),
    # classifiers=[
        # "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.6',
# )