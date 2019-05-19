package com.seatLight.bean;

import java.sql.Date;

public class BookInfo {

    private Integer num;
    private Integer state;
    private Date time;


    public Integer getNum() {
        return num;
    }

    public void setNum(Integer num) {
        this.num = num;
    }

    public Integer getState() {
        return state;
    }

    public void setState(Integer state) {
        this.state = state;
    }

    public Date getTime() {
        return time;
    }

    public void setTime(Date time) {
        this.time = time;
    }

    public BookInfo() {
    }

    public BookInfo(Integer num, Integer state, Date time) {
        this.num = num;
        this.state = state;
        this.time = time;
    }

    @Override
    public String toString() {
        return "BookInfo{" +
                "num=" + num +
                ", state=" + state +
                ", time=" + time +
                '}';
    }
}
