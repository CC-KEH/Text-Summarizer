import setuptools

SRC_REPO = 'txt_sm'
REPO_NAME = 'Text-Summarizer'
AUTHOR_USER_NAME = 'CC-KEH'
AUTHOR_EMAIL = 'cckeh08@gmail.com'
__version__ = '0.0.0'
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Python Project for Text Summarization',
    long_description='text/markdown',
    url=f'https.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)