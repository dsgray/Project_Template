# create environment and install requirements
echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda init bash
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
conda init bash
# conda activate /Users/davidgray/Documents/Data_Science/Project_Template/env
conda activate /Users/davidgray/Documents/Data_Science/Project_Template/env
echo [$(date)]: "intalling dev requirements"
set SETUPTOOLS_ENABLE_FEATURES="legacy-editable" ; pip install -e .
pip install -r requirements_dev.txt
echo [$(date)]: "END"