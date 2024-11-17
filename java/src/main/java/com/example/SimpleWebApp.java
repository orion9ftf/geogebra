package com.example;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletHandler;

public class SimpleWebApp {
    public static void main(String[] args) throws Exception {
        Server server = new Server(8080);
        
        ServletHandler handler = new ServletHandler();
        server.setHandler(handler);
        
        handler.addServletWithMapping(SimpleServlet.class, "/*");
        
        server.start();
        System.out.println("Server started. Visit http://localhost:8080 in your browser.");
        server.join();
    }
}
