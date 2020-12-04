import subprocess
commands='''
mkdir fem_tutorial
cd fem_tutorial

mkdir tmp
cd tmp
git init
git remote add origin https://gitlab.dune-project.org/dune-fem/dune-fempy.git
git config core.sparsecheckout true
echo 'demos/' > .git/info/sparse-checkout
echo 'doc/'  >> .git/info/sparse-checkout
git pull origin master
cp doc/*.py doc/*.ipynb doc/*.hh doc/*.dgf ..
cd ..
rm -rf tmp
rm py2ipynb.py pandoc-formatting.py gitlab-formatting.py interpolation.py svg2pdf.py
'''
subprocess.check_output(commands, shell=True)
