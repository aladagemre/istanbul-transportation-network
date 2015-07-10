routes = read.csv("iett/resources/linelist.csv")
bus_routes = subset(routes, routes$type=="bus")
simple_bus_routes = bus_routes[, c("code","cdk_id")]
write.csv(simple_bus_routes, "iett/resources/bus_lines.csv")
