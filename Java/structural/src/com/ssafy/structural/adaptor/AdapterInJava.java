package com.ssafy.structural.adaptor;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class AdapterInJava {
	   public static void main(String[] args) {
	        // io
	        try(InputStream is = new FileInputStream("input.txt");
	            InputStreamReader isr = new InputStreamReader(is);
	            BufferedReader reader = new BufferedReader(isr)) {
	            while(reader.ready()) {
	                System.out.println(reader.readLine());
	            }
	        } catch (IOException e) {
	            throw new RuntimeException(e);
	        }
	    }
}
