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
    public static void main(String[] args) throws IOException {

        JdbcTemplate jdbcTemplate = Utils.getJdbcTemplate();

        String sql = "select * from bookseat";
        List<BookInfo> infoList = jdbcTemplate.query(sql, new BeanPropertyRowMapper<>(BookInfo.class));

        for (BookInfo bookInfo : infoList) {

            Long currentTime = new Date().getTime();
            Long startTime = bookInfo.getStartTime().getTime();

            if (currentTime >= startTime) {

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

                String urlNameString = "http://192.168.2.101/on";
                try {
                    URL url = new URL(urlNameString);
                    //打开url的连接
                    URLConnection conn = url.openConnection();
                    //设置连接属性
                    conn.setConnectTimeout(6 * 1000);
                    conn.connect();
                    conn.getInputStream();
                } catch (Exception e) {

                }

            } else if (currentTime < startTime) {
                continue;
            } else {
                new IOException().printStackTrace();
            }
        }
    }
}
