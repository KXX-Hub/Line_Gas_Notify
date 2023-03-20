# Ethereum gas Notify（以太坊Gas即時價格通知）

 本專案使用*Etherscan API + Line Notify API*進行以太坊價格通知，使用者填入自己期望的Gas值，即可即時收到Gas變化的通知
 
<img width="397" alt="截圖 2023-03-17 上午12 26 08" src="https://user-images.githubusercontent.com/72089746/226346912-72d782f5-448a-4983-846e-8f07940005c8.png">

 如需正常使用Gas Notify，你需要有以下資料：

- [Etherscan API Key](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics)

  1. 到[Etherscan API 網站](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics)申請帳號

  2. 點選個人資料**Etherscan API key**，複製API key
   <img width="705" alt="截圖 2023-03-20 下午8 45 35" src="https://user-images.githubusercontent.com/72089746/226342843-444395fe-2dd7-48c8-8c38-29e6327b2932.png">

- [Line Notify Token](https://notify-bot.line.me/zh_TW/)

  1.登入[Line Notify](https://notify-bot.line.me/zh_TW/)
  2.點選你連動的服務
 
  <img width="705" alt="截圖 2023-03-20 下午8 50 16" src="https://user-images.githubusercontent.com/72089746/226343794-ae136265-79a0-478c-8343-d6398f343606.png">
  
  3.授權Line Notify並將Line Notify加入你希望被通知的聊天室
  
  4.點選同意並連動
  
  5.點選發行權杖
  
  <img width="521" alt="截圖 2023-03-20 下午8 54 41" src="https://user-images.githubusercontent.com/72089746/226344841-dca4c0a9-2e62-48c9-ad67-a29e0e784381.png">
  
  6.複製權杖(Token)**注意！要立刻馬上複製，權杖只會顯示一次**

# 如何使用
  1.下載Release
  
  2.Run app.py
  
  3.將Etherscan Api Key 和 Line Notify token填入config.yml
  
  4.將自己期望的Gas值(Gwei)填入config.yml
  
  5.再執行一次app.py即可運行
  
# 結語

希望大家都能夠在第一時間收到Gas通知馬上進行交易，預祝各位在web3.0的路上旅途愉快。
如果有想要討論或者建議小弟的歡迎告訴我 97007ken@gmail.com
各位的回饋都是我繼續做開源分享的動力
