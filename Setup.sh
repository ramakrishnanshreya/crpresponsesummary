# setup.sh
mkdir -p ~/.streamlit/
echo "[server]\nheadless = true\nport = $PORT\n" > ~/.streamlit/config.toml
pip install --upgrade streamlit
