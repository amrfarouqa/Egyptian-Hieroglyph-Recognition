# Egyptian Hieroglyphic Recognition - KTU Masters Project

<img src="Images/thothlogo.png">

> Kaunas Technology University MSc Informatics Research Project

---

### Table of Contents

- [About the Project](#About-the-Project)
- [Demonstration](#demonstration)
- [Description](#description)
- [Setup Guide](#setup-guide)
- [Usage Examples](#usage-examples)
- [License](#license)
- [Author Info](#author-info)

---

## About the Project

This project is intended to the selection process to work for [Adeo Web](https://www.adeoweb.biz/). I implemented this project to show and demonstrate my skills with [Symfony 5.1.2](https://symfony.com/). I never took any training what so ever regarding Symfony before, i learned during the process of making the application using online tutorials and manuals. Overall I found it fun and interesting.

---

## Demonstration

- Hosted Demonstration - [What To Wear Today? - AdeoWeb](https://adeoweb.amrfarouqa.website)


---

## Description

Based on the weather of the city you request in Lithuania, What To Wear Today will recommend what to wear so that you don't feel too cold or too hot throughout the day. It will also provide what you should bring. For example it would recommend an umbrella on a rainy day.

#### Technologies

- PHP 7.1+ Version
- JSON
- MySQL 
- Apache Web Server
- Composer
- Symfony 5.1.2 Framework


#### How It Works

Before getting dressed in the morning, we typically check the weather in Lithuania. Is it going to downpour? Or be the most beautiful day of the year? And as much as we love good old Weather.com, it does not give us that much information. That's were WTWT comes in handy. WTWT is a service, which returns product recommendations depending on current weather in Lithuania using the third-party weather API [LHMT - Meteo.lt](https://api.meteo.lt/). Based on custom weather or cutom city this application suggests what to wear currently using stored products in database created using [php-faker-clothing](https://github.com/rauwebieten/php-faker-clothing).



---

## Setup Guide

#### Installation

- Import database [wtwt](https://github.com/amrfarouqa/adeoWeb-WTWT/blob/master/mySQL%20FIle/wtwt.sql) into local phpMyAdmin
- Clone adeoWeb-WTWT [Repo](https://github.com/amrfarouqa/adeoWeb-WTWT.git) 
- Change Directory to Cloned Folder
- Edit Database Credentials Line 32 [.env File](https://github.com/amrfarouqa/adeoWeb-WTWT/blob/master/.env). If you can't find it, you need to show hidden files on your system
- Run Command "composer install"
- Make Sure Apache Web Server and MySQL Database are Running
- Run Command "symfony server:start" or "symfony serve"
- Go to [localhost:8000](http://localhost:8000) or [http://127.0.0.1:8000](http://127.0.0.1:8000) to see adeoWeb-WTWT Application



---

## Usage Examples

- API Call Example By Custom City (2055 Cities Available): GET /searchByCity/cityName/kaunas
- API Call Example By Custom Weather (All Weather Conditions Available in meteo.lt): GET /searchByWeather/weatherType/fog

#### Example City Names

- Vilnius
- Kaunas
- Klaipeda
- Siauliai
- Minsk


#### Example Weather Conditions

- Clear
- Isolated-Clouds
- Scattered-Clouds
- Overcast
- Light-Rain
- Moderate-Rain
- Heavy-Rain
- Sleet
- Light-Snow
- Moderate-Snow
- Heavy-Snow
- Fog


---

## License

MIT License

Copyright (c) [2020] [amrfarouqa]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



---

## Author Info

- Email - [aamrfarouqaa@gmail.com](mailto:aamrfarouqaa@gmail.com)
- Website - [https://amrfarouqa.website](https://amrfarouqa.website)
