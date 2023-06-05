package com.ssafy.structural.chainofresponsibility;

public class Client {
    public static void main(String[] args) {
        // 1. 핸들러 생성
        Handler handler1 = new ProtocolHandler();
        Handler handler2 = new DomianHandler();
        Handler handler3 = new PortHandler();

        // 2. 핸들러 연결 설정 (handler1 → handler2 → handler3)
        handler1.setNext(handler2).setNext(handler3);

        // 3. 요청에 대한 처리 연쇄 실행
        String url1 = "http://www.youtube.com:80";
        System.out.println("INPUT: " + url1);
        handler1.run(url1);

        System.out.println();

        String url2 = "https://www.ssafy.com:9999";
        System.out.println("INPUT: " + url2);
        handler1.run(url2);

        System.out.println();

        String url3 = "http://localhost:8080";
        System.out.println("INPUT: " + url3);
        handler1.run(url3);
    }
}