curl -L -O  https://github.com/mch/python-ant/archive/refs/heads/master.zip
tar -xf master.zip
cd python-ant-master
python setup.py install
pip install pywin32
cd ..
del master.zip
rd /Q /s python-ant-master