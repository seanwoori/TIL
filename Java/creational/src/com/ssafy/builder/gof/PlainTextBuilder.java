package com.ssafy.builder.gof;

//Data 데이터들을 평범한 문자열로 변환해주는 빌더
public class PlainTextBuilder extends Builder {

 public PlainTextBuilder(Data data) {
     super(data);
 }

 @Override
 public String head() {
     return "";
 }

 @Override
 public String body() {
     StringBuilder sb = new StringBuilder();

     sb.append("Name: ");
     sb.append(data.getName());
     sb.append(", Age: ");
     sb.append(data.getAge());

     return sb.toString();
 }

 @Override
 public String foot() {
     return "";
 }
}