package com.ssafy.builder;

public class StringBuilderExample {

    public static void main(String[] args) {
        StringBuilder stringBuilder = new StringBuilder();
        String result = stringBuilder.append("StringBuilder").append(" builder").toString();
        System.out.println(result);
    }
}