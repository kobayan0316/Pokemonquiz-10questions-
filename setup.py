from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Pokemonquiz', # パッケージ名(プロジェクト名)
    packages=['Pokemonquiz'], # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    install_requires=['random'], # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    author='kobayan0316', # パッケージ作者の名前
    author_email='s2122026@stu.musashino-u.ac.jp', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/kobayan0316/Pokemonquiz-10questions-', # パッケージに関連するサイトのURL(GitHubなど)

