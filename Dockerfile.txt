FROM ubuntu
RUN apt update && apt install -y python3 pip git tesseract-ocr gnupg ca-certificates wget unzip firefox clamav clamav-daemon
RUN pip install streamlit selenium wget pytesseract joblib 
RUN pip install scikit-learn==1.0.2
RUN git clone https://github.com/riacd/Security_Project.git


RUN wget https://www.slimjet.com/chrome/download-chrome.php?file=files%2F103.0.5060.53%2Fgoogle-chrome-stable_current_amd64.deb
RUN apt install -y ./'download-chrome.php?file=files%2F103.0.5060.53%2Fgoogle-chrome-stable_current_amd64.deb'


RUN wget https://registry.npmmirror.com/-/binary/chromedriver/103.0.5060.53/chromedriver_linux64.zip
RUN unzip 'chromedriver_linux64.zip'
RUN mv chromedriver /usr/bin