package com.seatLight.demo;


import com.seatLight.bean.BookInfo;
import com.seatLight.utils.Utils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Date;
import java.util.List;

public class SeatLightRealize {
    public static void main(String[] args) throws IOException, InterruptedException {

        JdbcTemplate jdbcTemplate = Utils.getJdbcTemplate();

        while (true) {

            String sql = "select * from smart_deskstate";
            List<BookInfo> infoList = jdbcTemplate.query(sql, new BeanPropertyRowMapper<>(BookInfo.class));

            for (BookInfo bookInfo : infoList) {

                Integer num = bookInfo.getNum() - 100;
                Integer state = bookInfo.getState();

                String urlNameStringOff = "http://192.168.43." + num +"/off";
                String urlNameStringOn = "http://192.168.43." + num +"/on";

                if (state == 0) {

                    System.out.println(bookInfo);

                    //PoolingHttpClientConnectionManager connectionManager = new PoolingHttpClientConnectionManager();
                    ////定义连接池最大的连接数
                    //connectionManager.setMaxTotal(200);
                    ////定义主机的最大的并发数
                    //connectionManager.setDefaultMaxPerRoute(20);
                    //HttpGet httpGet = new HttpGet("http://192.168.2.101/on");
                    //HttpRequestBase httpRequestBase = httpGet;
                    //httpRequestBase.setHeader("User-Agent", "Mozilla/5.0");
                    //CloseableHttpClient httpClient = HttpClients.custom().setConnectionManager(connectionManager).build();
                    //httpClient.execute(httpRequestBase);

                    try {
                        URL url = new URL(urlNameStringOff);
                        //打开url的连接
                        URLConnection conn = url.openConnection();
                        //设置连接属性
                        conn.setConnectTimeout(6 * 1000);
                        conn.connect();
                        conn.getInputStream();
                    } catch (Exception e) {
                        System.out.println("connect error!");
                        continue;
                    }

                } else if (state == 1 || state == 2) {
                    try {
                        URL url = new URL(urlNameStringOn);
                        //打开url的连接
                        URLConnection conn = url.openConnection();
                        //设置连接属性
                        conn.setConnectTimeout(6 * 1000);
                        conn.connect();
                        conn.getInputStream();
                    } catch (Exception e) {
                        System.out.println("connect error!");
                        continue;
                    }
                } else {
                    continue;
                }
            }
            Thread.sleep(1000);
        }
    }
}
