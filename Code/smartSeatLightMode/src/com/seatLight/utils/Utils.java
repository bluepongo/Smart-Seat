package com.seatLight.utils;

import com.mchange.v2.c3p0.ComboPooledDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

public class Utils {
    private static DataSource ds = new ComboPooledDataSource();

    public static JdbcTemplate getJdbcTemplate() {
        return new JdbcTemplate(ds);
    }
}
