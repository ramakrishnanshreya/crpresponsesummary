# setup.sh
mkdir -p ~/.streamlit/
echo "[server]\nheadless = true\nport = $PORT\n" > ~/.streamlit/config.toml
pip install --upgrade streamlit
pip install streamlit==1.15.0
pip install pandas==1.3.3
pip install matplotlib==3.4.3

