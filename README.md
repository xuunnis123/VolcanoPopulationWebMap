# VolcanoPopulationWebMap
實作利用python folium模組套入圖層，panda處理json讀入文字

功能實作可以選擇不同圖層進行疊加
共有兩種圖層：
- volcanoes
  火山分佈套圖
- populaion
  人口分佈套圖

利用world.json與volcano.txt撈取相關資料再套到圖層上


Pre-Installation:
$ pip3 install folium
$ pip3 install panda

Pre-doc:
volcano.txt


火山海拔標準示意顏色：
'橘色':海拔小於0公尺
'紫色':海拔介在0與1000公尺間
'藍色':海拔介在1000與2000公尺間
'粉紅色':超過2000公尺

人口示意顏色：
'綠色' 人口數小於1千萬
'橘色' ：人口數介在1千萬～5千萬間
'紅色'：人口數大於5千萬







