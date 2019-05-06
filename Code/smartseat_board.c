#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#define SENSOR_PIN    13


/* 连接您的WIFI SSID和密码，这个9个设备可以一致 */
#define WIFI_SSID         "zzzzzth"
#define WIFI_PASSWD       "z835311413"


/* 产品的三元组信息，根据9个测试设备的三元组，每个设备都烧录不同的*/
#define PRODUCT_KEY       "a1a0U8pqiyT"
#define DEVICE_NAME       "toilet_01"
#define DEVICE_SECRET     "DX3fyCRg8GZ9RHe74XQkfYsIPsbGep3i"

/* LD线上环境域名和端口号，不需要改 */
#define MQTT_SERVER       PRODUCT_KEY".iot-as-mqtt.cn-shanghai.aliyuncs.com"
#define MQTT_PORT         1883
#define MQTT_USRNAME      DEVICE_NAME "&" PRODUCT_KEY

// TODO: MQTT连接的签名信息，哈希加密请以"clientIdtestdeviceName"+设备名称+"productKey"+设备模型标识+“timestamp123456789”前往http://tool.oschina.net/encrypt?type=2进行加密
// HMACSHA1_SRC  clientIdtestdeviceNamehuman04productKeya1rezUVs103timestamp123456789
#define CLIENT_ID         "test|securemode=3,timestamp=123456789,signmethod=hmacsha1|"
#define MQTT_PASSWD       "b162e0ce8b57922bad69bbd64ea752d790574520"

#define ALINK_BODY_FORMAT         "{\"id\":\"123\",\"version\":\"1.0\",\"method\":\"%s\",\"params\":%s}"
#define ALINK_TOPIC_PROP_POST     "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post"
#define ALINK_TOPIC_PROP_POSTRSP  "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post_reply"
#define ALINK_TOPIC_PROP_SET      "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/service/property/set"
#define ALINK_METHOD_PROP_POST    "thing.event.property.post"



unsigned long lastMs = 0;

WiFiClient    espClient;
PubSubClient  client(espClient);


void callback(char *topic, byte *payload, unsigned int length)
{
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    payload[length] = '\0';
    Serial.println((char *)payload);
    
    if (strstr(topic, ALINK_TOPIC_PROP_SET))
    {
        StaticJsonBuffer<100> jsonBuffer;
        JsonObject& root = jsonBuffer.parseObject(payload);
        if (!root.success())
        {
            Serial.println("parseObject() failed");
            return ;
        }


    }
}


void wifiInit()
{
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWD);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("WiFi not Connect");
    }
  
    Serial.println("Connected to AP");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    
    client.setServer(MQTT_SERVER, MQTT_PORT);   /* 连接WiFi之后，连接MQTT服务器 */
    client.setCallback(callback);
}


void mqttCheckConnect()
{
    while (!client.connected())
    {
        Serial.println("Connecting to MQTT Server ...");
        if (client.connect(CLIENT_ID, MQTT_USRNAME, MQTT_PASSWD))
      
        {
            
            Serial.println("MQTT Connected!");
            // client.subscribe(ALINK_TOPIC_PROP_POSTRSP);
            client.subscribe(ALINK_TOPIC_PROP_SET);
            Serial.println("subscribe done");
        }
        else
        {
            Serial.print("MQTT Connect err:");
            Serial.println(client.state());
            delay(5000);
        }
    }
}


void mqttIntervalPost()
{
    char param[32];
    char jsonBuf[128];
    
    sprintf(param, "{\"MotionAlarmState\":%d}", digitalRead(13));
    sprintf(jsonBuf, ALINK_BODY_FORMAT, ALINK_METHOD_PROP_POST, param);
    Serial.println(jsonBuf);
    client.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
}


void setup() 
{

    pinMode(SENSOR_PIN,  INPUT);
    /* initialize serial for debugging */
    Serial.begin(115200);
    Serial.println("Demo Start");

    wifiInit();
}

     
// the loop function runs over and over again forever
void loop()
{
    if (millis() - lastMs >= 5000)
    {
        lastMs = millis();
        mqttCheckConnect(); 
    
        /* 上报 */
        mqttIntervalPost();
    }
    
    client.loop();
    if (digitalRead(SENSOR_PIN) == HIGH){
    Serial.println("Motion detected!");
    delay(2000);
      }
    else {
    Serial.println("Motion absent!");
    delay(2000);
  }
  
}