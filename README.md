# README
## Bot para dizu

### Requisitos:
*  python3
*  selenium 
*  chromedriver
*  conta do Dizu
*  conta's do insta

### Para instalar o selenium com pip3:
    $ pip3 install selenium

### Para instalar o chromedriver (no linux) faça:
    $ wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
    $ unzip chromedriver_linux64_2.3.zip
    $ sudo cp chromedriver /usr/bin/chromedriver
    $ sudo chown root /usr/bin/chromedriver
    $ sudo chmod +x /usr/bin/chromedriver
    $ sudo chmod 755 /usr/bin/chromedriver

### Para conta no Dizu, altere no dizu_new.py no def starter()..
* login_dizu = seuEmail
*  senha_dizu = suaSenha

### Para conta do instagram, altere no contas1, mantendo o padrão de uma conta por linha
* seuEmail:suaSenha:username

### Após estes basta executar
    $ python3 dizu_new.py
    
### Ao inicio selecione qual a lista da's conta (1)

### Ou pode-se utilizar do script diretamente:
    $ ./bot.sh
