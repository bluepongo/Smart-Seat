srv=net.createServer(net.TCP) 
srv:listen(80,function(conn) 
    conn:on("receive",function(conn,payload) 
    print(payload) 
    local _, _, method, vars = string.find(payload, "([A-Z]+) /(.+) HTTP")
           if(vars == "off")then
                 gpio.write(0, gpio.HIGH)
                 conn:send("<h1> Light OFF.</h1>")
           elseif(vars == "on")then
                 gpio.write(0, gpio.LOW)
                 conn:send("<h1> Light ON.</h1>")
           end
    end) 
end)