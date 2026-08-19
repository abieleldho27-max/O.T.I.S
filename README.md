# O.T.I.S (Object Tracking Intelligent System) Robot


## Overview
This is my AI desk robot, OTIS. He will be able to answer questions and interact with the world around him.

## Hardware Components
Seeed Studio XIAO ESP32S3
2 MG90s servos (Continuous)
One 2.4-inch LCD screen (ILI9341, SPI)
One 5v lipo battery(at least 2500 mA)


## Architecture Workflow
The Serial Monitor uses ```Serial.readString()``` with ``` while (!Serial.available()){}``` to wait for input from the user. Then, when an input is received, a HTTP POST request is sent to a Python script as JSON containing all the necessary data, such as the prompt and model. This data, once received by the Python script, is sent to Ollama's REST API to a model that is hosted locally on my device through the requests library. Once the data is sent, the returned JSON is deserialized with the Python json library through ```json.loads()```, where just the response is returned to the ESP32 to be printed to the Serial Monitor.

## Features
- AI features like a chatbot that can answer questions.
- Remote-controlled mode
- Tank treads
- Animated eyes with an LCD screen that displays answers

## Tools Used
- Fusion 360
- KiCad
- Ollama
- Open Web UI
- C++
- Visual Studio Code
- Python


## BOM
| Item  | Quantity | Price  | Notes | Status  | Second Header |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Seeed Studio XIAO ESP32S3 | 1 | $30.00  | unsoldered | Recieved | [URL](https://www.aliexpress.us/item/3256807069484332.html?spm=a2g0o.productlist.main.1.5e538nyR8nyRwC&algo_pvid=3cf81073-371e-4107-bfcf-7ef943f786e0&algo_exp_id=3cf81073-371e-4107-bfcf-7ef943f786e0-0&pdp_ext_f=%7B%22order%22%3A%22350%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2130.71%2115.05%21%21%21206.00%21100.94%21%40210328df17867346334073814e0f6e%2112000058193275679%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895&curPageLogUid=gbFpM3sFDtw7&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007255799084%7C_p_origin_prod%3A)  |
| MG90S servos  | 2 | $7.01  | continuous  | received | [URL](https://www.aliexpress.us/item/3256808846705668.html?spm=a2g0o.productlist.main.2.4da0LTEuLTEu9X&algo_pvid=0649ddb2-3706-43e2-9b87-eca29aa3e9d9&algo_exp_id=0649ddb2-3706-43e2-9b87-eca29aa3e9d9-1&pdp_ext_f=%7B%22order%22%3A%22524%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%215.52%210.99%21%21%2137.02%216.67%21%4021033b3317867347367166463e0f75%2112000047652734084%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895%3BpisId%3A5000000210798120&curPageLogUid=jGfSA8QqnEHj&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009033020420%7C_p_origin_prod%3A) |
| 2.4 inch LCD screen  | 1 | $6.79  | ILI9341, SPI  | pending | [URL](https://www.aliexpress.us/item/3256809575069193.html?spm=a2g0o.productlist.main.6.c5657efaSHxR3K&algo_pvid=7a0ede4d-6a58-481e-a8b1-ccfb9fb33d85&algo_exp_id=7a0ede4d-6a58-481e-a8b1-ccfb9fb33d85-5&pdp_ext_f=%7B%22order%22%3A%224934%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%215.62%210.99%21%21%2137.70%216.65%21%4021032c8d17867348556666174e0e53%2112000050079449343%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895%3BpisId%3A5000000210798120&curPageLogUid=niaD92oU4YC9&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009761383945%7C_p_origin_prod%3A) |
| 5V battery w/ charger | 1 | $14.35  | >= 2500 mA | pending | [URL]([https://www.amazon.com/KBT-Battery-Charger-Connector-Devices/dp/B0DSPKQWLH/ref=sr_1_13?crid=Z8FHSNAEWED4&dib=eyJ2IjoiMSJ9.dOyjTr8IuarM2GPi4Jaa5sOhW4mgED7S8c5b8_T3Mm3cj7wrz5wZwfEOhfv74ecuNvQrZCavlFMcOx3Sx8puWqHZ7FrEugTCDFiLQAHMGTOjKEIASeJem6J_741wUWT6vgV8egu6jmN05o2xOJ-jCpdOtmutNAkaKd_VBapyeYP9eByiHS0Be9cjVLzXoW8iPloXheF8Y9edwCXHsNX0kok4rr8KbJNpJmNZoRFnt2g.TGIrXrS9215Vh3FJZfXM9SR4YI2mkbbnKZr1iiw4hA0&dib_tag=se&keywords=5v+volt+battery&qid=1786045062&sprefix=5v+volt+battery%2Caps%2C173&sr=8-13](https://www.aliexpress.us/item/3256810270891847.html?spm=a2g0o.productlist.main.1.5e378659tPF24y&algo_pvid=5e8e54b9-7410-41d2-8c15-f387f4e4c85e&algo_exp_id=5e8e54b9-7410-41d2-8c15-f387f4e4c85e-0&pdp_ext_f=%7B%22order%22%3A%22222%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2135.01%217.74%21%21%21234.84%2151.96%21%402101d33417867349832623310e0ff7%2112000052475977302%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895%3BpisId%3A5000000210798115&curPageLogUid=Rv1VAAKrkLdz&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005010457206599%7C_p_origin_prod%3A))|
| 22 AWG silicon wire  | 1 | $13.36  | 10 feet, 6 Colors  | Recieved  | [URL](http://aliexpress.us/item/2251832829997304.html?spm=a2g0o.productlist.main.4.35dc66felJC0yE&algo_pvid=8587cf42-78d5-4646-8451-cac24ebd9836&algo_exp_id=8587cf42-78d5-4646-8451-cac24ebd9836-33&pdp_ext_f=%7B%22order%22%3A%22451%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2113.36%212.03%21%21%2113.36%212.03%21%402103292b17867352043358113e0ce3%2167175045829%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895%3BpisId%3A5000000210798120&curPageLogUid=ZNsCRpi1rxmJ&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A33016312056%7C_p_origin_prod%3A) |
| 7-8 in Silicon Band | 2 | $3.50  | for tank treads  | pending  | [URL](https://www.aliexpress.us/item/3256806714457904.html?spm=a2g0o.productlist.main.41.602dI2GvI2GvA8&algo_pvid=2fe4a297-742d-401d-9b9f-e929d2f2b626&algo_exp_id=2fe4a297-742d-401d-9b9f-e929d2f2b626-40&pdp_ext_f=%7B%22order%22%3A%22159%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.52%210.99%21%21%2123.60%216.62%21%4021030f4a17871769171935865e0cee%2112000038659934063%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ab0a929c1%3Bm03_new_user%3A-29895%3BpisId%3A5000000210798120&curPageLogUid=zoLVYdqQ5KBg&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006900772656%7C_p_origin_prod%3A)   |
| 0V5640 camera with heatsinks  | 1 | $22.89  | for cooling  | bought | [URL](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/114993115/21277047)  |
| M2.5 x 6 mm screws | 4  | $2.00 | buy in person  | pending  | N/A |

## Photos
<img width="582" height="585" alt="OTIS final assembly pic" src="https://github.com/user-attachments/assets/e345d0a8-cb3e-4a03-abb7-2c6401ea3f3f" />
<img width="1577" height="1117" alt="Screenshot 2026-08-19 180911" src="https://github.com/user-attachments/assets/ce4d9846-0b56-4aaa-80c9-432f2ff1d5df" />
<img width="1754" height="737" alt="Screenshot 2026-08-04 191854" src="https://github.com/user-attachments/assets/9b0d4c6f-b86b-4e72-aaf2-417bfd7d45d5" />




Total Cost = $110 - $120
## Status
I have completed the design and have submitted the project for funding.
## Author 
Abiel Eldho
