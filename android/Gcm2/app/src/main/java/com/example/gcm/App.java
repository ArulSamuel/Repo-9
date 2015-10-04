package com.example.gcm;

/**
 * Created by Arul on 10/3/2015.
 */
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.example.gcm.vo.Content;

public class App
{
    public static void main( String[] args )
    {
        System.out.println( "Sending POST to GCM" );

        String apiKey = "AIzaSyC6fBEo-dJbt4HOZUXX_myNnEr_ZWYO8is";
        Content content = createContent();

        POST2GCM.post(apiKey, content);
    }

    public static Content createContent(){

        Content c = new Content();

        c.addRegId("My reg ID ARUL :) ");
        c.createData("Test Title", "Test Message");

        return c;
    }
}