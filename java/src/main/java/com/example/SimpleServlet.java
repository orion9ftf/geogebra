package com.example;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class SimpleServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        String message = request.getParameter("message");
        
        out.println("<html><body>");
        out.println("<h1>Simple Message Input</h1>");
        out.println("<form method='get'>");
        out.println("Message: <input type='text' name='message'>");
        out.println("<input type='submit' value='Send'>");
        out.println("</form>");
        
        if (message != null && !message.isEmpty()) {
            out.println("<h2>Message sent: " + message + "</h2>");
        }
        
        out.println("</body></html>");
    }
}
