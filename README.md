#O.T.I.S (Object Tracking Intelligent System) Robot


## Overview
This is my AI desk robot, OTIS. He will be able to answer questions and interact with the world around him.

## Hardware Components
Seeed Studio XIAO ESP32S3
2 MG90s servos (Continuous)
One 2.4-inch LCD screen (ILI9341, SPI)
One 5v lipo battery(at least 2500 mA)


## Architecture Workflow
The ESP32 will send the prompt as a request to Ollama's REST API through WiFi, which I will utilize to install and run local AI models on my PC. Then I can receive the response and print it onto the LCD.

## Features
- AI features like a chatbot that can answer questions.
- Remote controllable mode
- Tank treads
- Animated eyes with an LCD screen that displays answers

## Tools Used
- Fusion 360
- KiCad


## BOM
| Item  | Quantity | Price  | Notes | Status  | Second Header |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Seeed Studio XIAO ESP32S3 | 1 | $23.99  | unsoldered | bought | [URL](https://www.amazon.com/Seeed-Studio-XIAO-ESP32-Sense/dp/B0DRNW6KMG/ref=sr_1_1_sspa?crid=9FPLHFR1KT5I&dib=eyJ2IjoiMSJ9.c_bkuo_mWg_7Ypo9HgDeWHXlr94Z3KrGQXkatpPpKFW-foMtNknm4-E54DbxEOUu_9Vts1TTdYTQIy8w08_iVvzAP1Sy6pzB5LMI2kkmwYaoXCSv7HmKmdQ9Xqz0F3CPOZD4wmQQAhP76XrB-ZxjVmdR1gy_ThzGia9t9yEjjEW82BzHBXMw0TCZXHszQOz8vKbu_6fI9wBN6NCFmd5ncUQ0wOvl6ns8nwwuiL1WPsE.6KivbGpg5le90qjGVio_y2SpIBTyZkVgluygz8OM38w&dib_tag=se&keywords=seeed%2Bstudio%2Bxiao%2Besp32-s3&qid=1785526701&sprefix=seeed%2B%2Caps%2C167&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)  |
| MG90S servos  | 2 | $8.68  | continuous  | pending | [URL](https://www.amazon.com/DiGiYes-MG90S-Helicopter-Airplane-Controls/dp/B0BHYH7MQK/ref=sr_1_2?crid=31ELWDCIJNVPV&dib=eyJ2IjoiMSJ9.yE3g4FMJg171jE-uEvgiYSVz3Q8ZbTTjNJc5b_5FOGau9X6TiQDlR4C5F2iNQuzJkcl-q-5QXqtjVRXmQEqIYMMzPmpfqUz6ryhqMjMxkPQ.fI0TWUJmVf9BX-UkKCj_9pOoDHcUFBI5270rQgk_7pc&dib_tag=se&keywords=DIGIyes%2Bmg90s&qid=1785526764&sprefix=digiyes%2Bmg90%2Caps%2C146&sr=8-2&th=1) |
| 2.4 inch LCD screen  | 1 | $18.99  | ILI9341, SPI  | pending | [URL](https://www.amazon.com/Waveshare-2-4inch-Display-Resolution-Interface/dp/B08H24H7KX/ref=sr_1_8?crid=2VD3AG6JFDYF8&dib=eyJ2IjoiMSJ9.6kWIg5X_HOAB4622JzmdDU5eAy3tdFKqsurkNHd8uIQhiP8NVeMi0vTThd9KnVyI4owrmmvnIrLGKkxT_AmuLPocGFNiUrIr8NYGNAy5_ta9-aMEoO-kFqHGJSTn1XTVzSqnMC6y2n2XIfFG4TMeehotpxwTT8zr95vzC9Vpt51p-feR0oPnm8mkmGwv4CR-haNfrJ5vvPX2ocuRzn8vozaoEuQfOkj61BXXL95g_nM.AvgHdp8uQGKk0MtuGeSiE8zxU1KjS1BOUVb-xyU_Lh8&dib_tag=se&keywords=2.4%2Binch%2Blcd%2Bscreen&qid=1785526170&sprefix=2.4%2Binch%2Blcd%2Bscreen%2Caps%2C222&sr=8-8&th=1) |
| 5V lipo battery w/ charger | 1 | pending  | >= 2500 mA | pending | pending|
| Jumper Wires  | N/A | N/A  | I may need more | Owned | N/A |
| 22 AWG silicon wire  | N/A | pending  | 10 feet, 6 Colors  | bought  | [URL](https://www.amazon.com/Fermerry-Stranded-Electric-Tinned-Copper/dp/B089CQHRDT/ref=sr_1_3?crid=KLSZ1ZDXWGY2&dib=eyJ2IjoiMSJ9.oeeUQJ2LTZ-VwFsfQT-ZAWTVqMXBkRL5yKXS-uGMkMEPjBblSwKZU-rdQH1_pZxyW2UPTyrn7TtdNXS20HSmEboiQv7_nj67e7I5MFv3sCRvqx4XssBSLtx9jvvU-S9ZCW7RJCEheyoOViEdKZp0jtTiA4hrn3EVL_xUo-52-l2_jzEH7MXuC2ldnF1lkWGEEmYEu-6IxoHo5HRP9OHfK76QGcfhw98ZNwN0WULLrf6qfIpxVijEURpsSYdQdK9vKGYH71vH_oUsp0zm5PWo5AzO3ihdw7zdlbZEKMXeG0w.wbYbzcMBKuUzNa3--WXpwA1LlIOrx5blzw269HrbfWE&dib_tag=se&keywords=digigo%2B22AWG%2Bwire&qid=1785791428&sprefix=digigo%2B22awg%2Bwir%2Caps%2C278&sr=8-3&th=1) |
| 70X037 Timing belt  | 2 | $7.79  | for tank treads  | pending  | [URL](https://www.amazon.com/uxcell-Timing-Rubber-Geared-Synchronous/dp/B0DDTW9QG8/ref=sr_1_10?dib=eyJ2IjoiMSJ9.3nmsI9fbEu8SxQ8-RCJpXbn-j8OR7hvIyYbGMYbKXMiF2iofdXKRgUzDdUhcbMoHD5TRjL5AolAt2Wvx7-GwtuOKiKbzZl7BCYhmRLzwhHzB88F-0M94pVQpg6n8Ave_6_JZHG_Tdp-XUyQoJ1bpyJ_UmFy9J-6mZ9NY-YkzrUjDBDgcu3UT_2-_BbDYXpQpQYVf7pAjDvyICZs8n9oA3gWfBhBbud01yxarYVU4Zlk.WJM4c9CTRseO3v-9pRRjnjVGMuAdRr1m3rvqV4JFrtE&dib_tag=se&keywords=Rubber%2BTiming%2BBelt%2BToothed%2BTeeth&qid=1785596066&sr=8-10&th=1)   |
| 0V5640 camera with heatsinks  | 1 | $12.99  | for cooling  | pending | [URL](https://www.seeedstudio.com/OV5640-Camera-for-XIAO-ESP32S3-Sense-With-Heat-Sink-p-5739.html)  |
| M2.5 x 6 mm screws | 4  | pending | buy in person  | pending  | N/A |


