# Structure of HTTP Message

1. Start Line(Request/Status)
    1. Request Message : Request Line
    2. Response Message : Status Line
        1. Example of Start Line
        - GET /comics/marvel/Ironman HTTP/1.1
        - REQUEST METHOD(GET/POST) + TARGET URL + PROTOCOL VERSION

2. Header
    1. CRLF(Carriage Return Line Feed) exists on Each Line of the Header

    [https://serverfault.com/questions/197571/what-does-crlf-mean/197574](https://serverfault.com/questions/197571/what-does-crlf-mean/197574)

    1. Example Of Header
        - HOST : www.example.com:8888
        - NAME : VALUE

3. Blank Line ———————-The Border Between Header And Body——————————
4. Body

<Both Header and Body can be omitted when communicate>

## Various Types Of HTTP REQUEST METHODS

[HTTP METHODS](https://www.notion.so/1d4b0bfec0a04a57b2e135346824fa2e)

### The Two Commonly Used Method For HTML FORM

```jsx
GET : [https://www.example.com/search/?q=forms&release=10](https://www.example.com/search/?q=forms&release=10) HTTP/1.1
```

```jsx
POST : [https://www.example.com/search/](https://www.example.com/search/) HTTP/1.1
Content-Type : application/x-www-form-urlencoded

q=forms&release=10
```

Due to the Difference of Parameter Sending Mechanism, 

Using Get Method will be much more difficult to send massive amount of datas than Using POST.

Because GET Method has limited URL Length Support 

The Data that user send will be exposed to its web-browser's URL ADDRESS FORM.

## STATUS CODE

[STATUS CODE TYPES](https://www.notion.so/3e288087395549d0a3bec2728ba3aabf)

[https://www.guru99.com/url-vs-uri-difference.html#2](https://www.guru99.com/url-vs-uri-difference.html#2)

Useful Reference to know the difference between URL and URI(301).

## URL DESIGN

[https://www.example.com:75/services?category=2&kind=target#num10](https://www.example.com:75/services?category=2&kind=target#num10)

1. URL Scheme - https // http [https://www.guru99.com/difference-http-vs-https.html](https://www.guru99.com/difference-http-vs-https.html)
    - The Protocol Used For URL
2. Host Name - www. example.com
    - The Host Name Of Web Server, Expressed by Domain Name or IP Address
3. Port Number - :75
    - The Service Port Number inside of its Backend WebServer, if its omitted - > default portnumber applied // http → 80 https → 443
4. Path - /services
    - The Internal Path of File or Application
5. Query String(Question) - ?category2=&kind=target
    - Question To The DataBase Exist Distinguished By & Name (=) Value
6. Fragments - #num10
    - Select the Anker or Fragmant on the existing Documents.

### Type of URL

1. RPC(Remote Procedure Call) : The method which Client Call the API Function via Remote Server exist in the Network.
2. REST(Representational State Transfer)  : It Consider Every Factors as Resources and Express it as certain URL.

    (As time flows, the State of Resource can be diversified so the interaction between client and server deemed as Representational State Transfer)

    (The Resource Manipulation Events are created by GET,POST,PUT,Delete —- etc, HTTP Methods)
