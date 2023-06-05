package com.ssafy.structural.adaptor;

//Adapter : Adaptee 서비스를 클라이언트에서 사용하게 할 수 있도록 호환 처리 해주는 어댑터
public class Adapter implements Target {
 Service adaptee; // composition으로 Service 객체를 클래스 필드로

 // 어댑터가 인스턴스화되면 호환시킬 기존 서비스를 설정
 Adapter(Service adaptee) {
     this.adaptee = adaptee;
 }

 // 어댑터의 메소드가 호출되면, Adaptee의 메소드를 호출하도록
 public void method(int data) {
     adaptee.specificMethod(data); // 위임
 }
}