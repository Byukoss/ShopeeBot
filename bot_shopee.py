import requests
from bs4 import BeautifulSoup

def raspar_ofertas():
    url = "https://shopee.com.br/ofertas-do-dia"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ajuste o seletor conforme o HTML da Shopee (pode mudar!)
    for produto in soup.select('div[data-sqe="item"]'):  
        nome = produto.select_one('div[data-sqe="name"]').text.strip()
        preco_original = produto.select_one('.W6yNIr').text.strip()
        preco_promocional = produto.select_one('.ZEgDH9').text.strip()
        link_relativo = produto.find('a')['href']
        link_completo = f"https://shopee.com.br{link_relativo}"
        
        print(f"🎁 {nome}")
        print(f"💰 De: {preco_original} → Por: {preco_promocional}")
        print(f"🔗 {link_completo}\n")

raspar_ofertas()

AFFILIATE_ID = "18331590616"  # Substitua pelo seu ID do Shopee Affiliate

def gerar_link_afiliado(link_original):
    return f"{link_original}?affiliate_id={AFFILIATE_ID}"

from telegram import Bot
import asyncio

TOKEN = "8071966449:AAH8YNwrlQgQZmW_OSpiogxvsusvuhRRymU"
CHAT_ID = "-1002357173260"  # Ou ID do grupo

async def enviar_para_telegram(mensagem):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown")

# Exemplo de uso:
mensagem = f"""
🔥 *PROMOÇÃO SHOPEE* 🔥  
*Nome*: {nome}  
*De*: {preco_original} → *Por*: {preco_promocional}  
[🛒 Comprar aqui]({link_afiliado})  
"""
asyncio.run(enviar_para_telegram(mensagem))
