if command -v deactivate &> /dev/null; then
    source deactivate
fi

python3 -m venv venv
source venv/bin/activate
pip install -r out/python/requirements.txt